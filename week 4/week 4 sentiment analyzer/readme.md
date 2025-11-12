# Sentiment Analysis System 
## Overview 
This project implements sentiment analysis for product reviews using Natural Language 
Processing (NLP) techniques from Chapter 23. 
## Features - **Two Analysis Methods:** - Simple: Word counting based on positive/negative word lists - Advanced: Machine learning using TextBlob - **REST API** for easy integration - **Visualization** of sentiment distributions - **Text preprocessing** including tokenization and stop word removal 
## How to Run 
### 1. Install Requirements 
```bash 
pip install -r requirements.txt 
``` 
### 2. Test the Analyzer 
```bash 
python test_sentiment.py 
``` 
### 3. Start the API Server 
```bash 
python api_server.py 
``` 
Then visit http://localhost:5000 
## API Usage Example 
```python 
import requests 
response = requests.post('http://localhost:5000/analyze', 
json={'text': 'This product is amazing!'}) 
print(response.json()) 
``` 
## Understanding NLP Concepts 
### Tokenization 
Breaking text into words: "I love this" → ["I", "love", "this"] 
### Stop Words 
Common words we filter out: "the", "is", "at", "which" 
### Sentiment Analysis 
Determining if text is positive, negative, or neutral 
## Challenges Encountered 
Handling Neutral Sentiment: The model initially struggled to classify neutral reviews accurately. I improved this by refining the training data and adjusting the preprocessing to preserve more context.
## Real-World Applications 
Customer Feedback Analysis-Companies use sentiment analysis to monitor reviews and social media to improve products and services.
Brand Reputation Management- It helps track public sentiment toward a brand in real time, especially during PR crises.
Market Research- Businesses analyze sentiment trends to understand consumer preferences and forecast demand.
## What I Learned 
I now understand how Natural Language Processing (NLP) breaks down human language into structured data. Tokenization splits text into meaningful units, while sentiment analysis uses labeled data to classify emotional tones. This project enhanced my skills in Python programming, API development, and data visualization, providing a solid foundation for future NLP endeavors.
