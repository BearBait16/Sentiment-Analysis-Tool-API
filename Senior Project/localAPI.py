from flask import Flask, request, jsonify
from transformers import pipeline
from passlib.hash import argon2
from argon2 import PasswordHasher
import secrets
import psycopg2 

# Just to make sure that it's working
app = Flask(__name__)

# Sets up the pipeline so that the server can run the requests faster
pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")    

# Runs the connection to the local db during flask run stuff
conn = psycopg2.connect(
    dbname ="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
# Sets up connection to the Database
cur = conn.cursor()

# Sets up Argon2 hashing
ph = PasswordHasher()

# Browser Check
@app.route('/')
def home():
    return "It's working"



# Single review sentiment
@app.route('/single_sentiment', methods=['POST'])
def singleSentiment():
    isVerified = authentication()
    if isVerified:
        data = request.get_json()
        review = data['text']
        result = pipe(review)
        addSingleAPIUse() 
        return jsonify({"review": review, "sentiment": result})
    else:
        return jsonify({"Error": "AUTHENTICATION FAILURE"})



# Batch review sentiment
@app.route('/batch_sentiment', methods=['POST'])
def batchSentiment():
    isVerified = authentication()
    if isVerified:
        data = request.get_json()
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
@app.route('/user_creation', methods=['POST'])
def userCreation():
    data = request.get_json()
    userId = 2
    username = data['name']
    password = data['password']
    hashedpassword = argon2.hash(password)
    apiKey, hashed_key = generateAPIKey() # One to store, and one to return to user.
    apiUsage = 0
    apiMessage = "Copy this, keep it secret, keep it safe"
    insert_query = """
    INSERT INTO users(user_id, user_name, password, api_key, api_usage)
    VALUES(%s, %s, %s, %s, %s)
    """
    cur.execute(insert_query, (userId, username, hashedpassword, hashed_key, apiUsage))
    conn.commit()
    return jsonify(apiKey, apiMessage)



# Generates an API key for a user
def generateAPIKey():
    apiKey = secrets.token_urlsafe(32)
    hashed_key = ph.hash(apiKey) # Hashes the api, returning both.
    return apiKey, hashed_key



# User Authentication for API usage
def authentication():
    username = request.headers.get("x-username")
    api_key = request.headers.get("x-api-key") # Checks the header for a api key 
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
def addSingleAPIUse():
    username = request.headers.get("x-username")
    update_query = """
UPDATE users 
SET api_usage = api_usage + 1
WHERE user_name = %s;
"""
    cur.execute(update_query, (username,))
    conn.commit()



def addBatchAPIUse(uses):
    username = request.headers.get("x-username")
    update_query = """
UPDATE users 
SET api_usage = api_usage + %s
WHERE user_name = %s;
"""    
    cur.execute(update_query, (uses, username))
    conn.commit()

# Basic Running of the API
if __name__ == '__main__':
    app.run(debug= True)