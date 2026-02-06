from flask import Flask, request, jsonify
from transformers import pipeline
from passlib.hash import argon2
import hashlib
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
cur = conn.cursor()

@app.route('/')
def home():
    return "Hello World!"

# Single review sentiment
@app.route('/single_sentiment', methods=['POST'])
def singleSentiment():
    data = request.get_json()
    review = data['text']
    result = pipe(review)
    return jsonify({"review": review, "sentiment": result})

# Batch review sentiment
@app.route('/batch_sentiment', methods=['POST'])
def batchSentiment():
    data = request.get_json()
    reviews = {}
    for review in data:
        reviewID = review['id']
        reviewText = review['text']
        result = pipe(reviewText)
        print(f"ID: {reviewID}, Review:{reviewText}, Result:{result}")
        reviews[reviewID] = result
    return jsonify(reviews)

@app.route('/user_creation', methods=['POST'])
def userCreation():
    data = request.get_json()
    userId = 2
    username = data['name']
    password = data['password']
    password = argon2.hash(password)
    apiKey, hashed_key = generateAPIKey()
    apiUsage = 0
    apiMessage = "Copy this, keep it secret, keep it safe"
    insert_query = """
    INSERT INTO users(user_id, user_name, password, api_key, api_usage)
    VALUES(%s, %s, %s, %s, %s)
    """
    cur.execute(insert_query, (userId, username, password, hashed_key, apiUsage))
    conn.commit()
    return jsonify(apiKey, apiMessage)

def generateAPIKey():
    apiKey = secrets.token_urlsafe(32)
    hashed_key = hashlib.sha256(apiKey.encode()).digest()
    return apiKey, hashed_key

if __name__ == '__main__':
    app.run(debug= True)