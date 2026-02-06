from transformers import pipeline
pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")      
prompt = input("Please paste the review for sentiment analysis: ")
result = pipe(prompt)
print(result)