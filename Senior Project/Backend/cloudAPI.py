from transformers import pipeline
from passlib.hash import argon2
from argon2 import PasswordHasher
import secrets
import psycopg2 
import jsonify
import json

# Sets up the pipeline so that the server can run the requests faster
pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")    

# Runs the connection to the local db during flask run stuff
conn = psycopg2.connect(
    dbname ="mydb",
    user="user",
    password="wouldn't you like to know weather boy",
    host="ip-172-31-20-171.us-west-2.compute.internal",
    port="5432",
    sslmode="require"
)
# Sets up connection to the Database
cur = conn.cursor()

# Sets up Argon2 hashing
ph = PasswordHasher()



# Single review sentiment
def singleSentiment(event):
    if not authentication(event):
        return jsonify({"Error": "AUTHENTICATION FAILURE"})
    
    data = json.loads(event["body"])
    review = data['text']
    result = pipe(review)
    addSingleAPIUse() 
    return jsonify({"review": review, "sentiment": result})




# Batch review sentiment
def batchSentiment(event):
    isVerified = authentication()
    if isVerified:
        data = json.loads(event["body"])
        reviews = {}
        for review in data:
            reviewID = review['id']
            reviewText = review['text']
            result = pipe(reviewText)
            print(f"ID: {reviewID}, Review:{reviewText}, Result:{result}")
            reviews[reviewID] = result
        uses = reviews.__len__()
        addBatchAPIUse(uses)
        return jsonify(reviews)
    else:
        return jsonify({"Error": "AUTHENTICATION FAILURE"})



# User Creation
def userCreation(event):
    data = json.loads(event["body"])
    username = data['name']
    password = data['password']
    hashed_password = argon2.hash(password)
    apiKey, hashed_key = generateAPIKey() # One to store, and one to return to user.
    apiUsage = 0 # Hard Codes Default 0 API uses
    apiMessage = "Copy this, keep it secret, keep it safe"
    insert_query = """
    INSERT INTO users (user_name, password, api_key, api_usage)
    VALUES( %s, %s, %s, %s)
    """
    cur.execute(insert_query, (username, hashed_password, hashed_key, apiUsage))
    conn.commit()
    return jsonify(apiKey, apiMessage)



# Generates an API key for a user
def generateAPIKey():
    apiKey = secrets.token_urlsafe(32)
    hashed_key = ph.hash(apiKey) # Hashes the api, returning both.
    return apiKey, hashed_key



# User Authentication for API usage
def authentication(event):
    headers = event.get("headers", {})
    username = headers.get("x-username")
    api_key = headers.get("x-api-key") # Checks the header for a api key 
    if api_key == None: # If none are provided, immidiatley sends an error
        return False
    check_query = """
SELECT api_key
FROM users
WHERE user_name = %s
"""
    cur.execute(check_query, (username,))
    row = cur.fetchone()
    if row == None:
        return False
    storedHash = row[0]
    isVerified = ph.verify(storedHash, api_key)
    return isVerified



# A funciton that handles adding a use to the database
def addSingleAPIUse(event):
    headers = event.get("headers", {})
    username = headers.get("x-username")
    update_query = """
UPDATE users 
SET api_usage = api_usage + 1
WHERE user_name = %s;
"""
    cur.execute(update_query, (username,))
    conn.commit()



def addBatchAPIUse(event, uses):
    headers = event.get("headers", {})
    username = headers.get("x-username")
    update_query = """
UPDATE users 
SET api_usage = api_usage + %s
WHERE user_name = %s;
"""    
    cur.execute(update_query, (uses, username))
    conn.commit()

def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

def lambda_handler(event, context):

    path = event.get("rawPath")
    method = event.get("requestContext", {}).get("http", {}).get("method")

    try:
        if path == "/":
            return response(200, "It's working")

        elif path == "/single_sentiment" and method == "POST":
            return single_sentiment(event)

        elif path == "/batch_sentiment" and method == "POST":
            return batch_sentiment(event)

        elif path == "/user_creation" and method == "POST":
            return user_creation(event)

        else:
            return response(404, {"error": "Route not found"})

    except Exception as e:
        return response(500, {"error": str(e)})