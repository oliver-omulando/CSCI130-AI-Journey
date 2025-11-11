# sentiment_analyzer.py 
from textblob import TextBlob 
import pandas as pd 
import re 
from collections import Counter 
import nltk 
nltk.download('punkt', quiet=True) 
nltk.download('stopwords', quiet=True) 
from nltk.corpus import stopwords 
import matplotlib.pyplot as plt 
 
class SentimentAnalyzer: 
    """ 
    Analyzes sentiment in text reviews 
    Demonstrates NLP concepts from Chapter 23 
    """ 
     
    def __init__(self): 
        self.stop_words = set(stopwords.words('english')) 
        self.positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful', 
                               'fantastic', 'love', 'best', 'perfect', 'happy'} 
        self.negative_words = {'bad', 'terrible', 'awful', 'horrible', 'worst', 
                               'hate', 'disappointing', 'useless', 'waste', 'poor'} 
     
    def preprocess_text(self, text): 
        """ 
        Clean and prepare text for analysis 
        This is tokenization and normalization! 
        """ 
        # Convert to lowercase 
        text = text.lower() 
         
        # Remove special characters but keep spaces 
        text = re.sub(r'[^a-z\s]', '', text) 
         
        # Split into words (tokenization) 
        words = text.split() 
         
        # Remove stop words 
        words = [w for w in words if w not in self.stop_words] 
         
        return words 
     
    def analyze_sentiment_simple(self, text): 
        """ 
        Simple sentiment analysis using word counting 
        This is a rule-based approach 
        """ 
        words = self.preprocess_text(text) 
         
        positive_count = sum(1 for word in words if word in self.positive_words) 
        negative_count = sum(1 for word in words if word in self.negative_words) 
         
        # Determine sentiment 
        if positive_count > negative_count: 
            sentiment = "Positive" 
            confidence = (positive_count / (positive_count + negative_count + 1)) * 100 
        elif negative_count > positive_count: 
            sentiment = "Negative" 
            confidence = (negative_count / (positive_count + negative_count + 1)) * 100 
        else: 
            sentiment = "Neutral" 
            confidence = 50 
         
        return { 
            'sentiment': sentiment, 
            'confidence': confidence, 
            'positive_words_found': positive_count, 
            'negative_words_found': negative_count 
        } 
     
    def analyze_sentiment_advanced(self, text): 
        """ 
        Advanced sentiment using TextBlob library 
        This uses machine learning under the hood! 
        """ 
        blob = TextBlob(text) 
         
        # Get polarity score (-1 to 1) 
        polarity = blob.sentiment.polarity 
         
        # Convert to sentiment label 
        if polarity > 0.1: 
            sentiment = "Positive" 
        elif polarity < -0.1: 
            sentiment = "Negative" 
        else: 
            sentiment = "Neutral" 
         
        # Calculate confidence (0 to 100) 
        confidence = abs(polarity) * 100 
         
        return { 
            'sentiment': sentiment, 
            'polarity': polarity, 
            'confidence': min(confidence, 100), 
            'subjectivity': blob.sentiment.subjectivity 
        } 
     
    def analyze_multiple_reviews(self, reviews): 
        """Analyze multiple reviews and show statistics""" 
        results = [] 
         
        for review in reviews: 
            simple = self.analyze_sentiment_simple(review) 
            advanced = self.analyze_sentiment_advanced(review) 
             
            results.append({ 
                'review': review[:50] + '...' if len(review) > 50 else review, 
                'simple_sentiment': simple['sentiment'], 
                'advanced_sentiment': advanced['sentiment'], 
                'polarity': advanced['polarity'] 
            }) 
         
        df = pd.DataFrame(results) 
         
        # Show summary statistics 
        print("\n📊 SENTIMENT ANALYSIS RESULTS") 
        print("=" * 50) 
        print("\nSimple Method Results:") 
        print(df['simple_sentiment'].value_counts()) 
        print("\nAdvanced Method Results:") 
        print(df['advanced_sentiment'].value_counts()) 
         
        return df 
     
    def visualize_sentiment(self, reviews): 
        """Create visualizations of sentiment analysis""" 
        # Analyze all reviews 
        polarities = [] 
        sentiments = [] 
         
        for review in reviews: 
            result = self.analyze_sentiment_advanced(review) 
            polarities.append(result['polarity']) 
            sentiments.append(result['sentiment']) 
         
        # Create visualization 
        fig, axes = plt.subplots(1, 2, figsize=(12, 5)) 
         
        # Plot 1: Sentiment Distribution 
        sentiment_counts = Counter(sentiments) 
        axes[0].bar(sentiment_counts.keys(), sentiment_counts.values(), 
                   color=['green', 'gray', 'red']) 
        axes[0].set_title('Sentiment Distribution') 
        axes[0].set_ylabel('Number of Reviews') 
         
        # Plot 2: Polarity Scores 
        axes[1].hist(polarities, bins=20, edgecolor='black') 
        axes[1].set_title('Polarity Score Distribution') 
        axes[1].set_xlabel('Polarity (-1 = Negative, +1 = Positive)') 
        axes[1].set_ylabel('Count') 
        axes[1].axvline(x=0, color='red', linestyle='--', alpha=0.5) 
         
        plt.tight_layout() 
        plt.savefig('sentiment_visualization.png') 
        print("\n📈 Saved visualization as 'sentiment_visualization.png'") 
        return fig


if __name__ == '__main__':
    # Small demo runner with example reviews
    sample_reviews = [
        "I love this product! It's amazing and works perfectly.",
        "Terrible experience. This is the worst. I hate it.",
        "It was okay, nothing special."
    ]

    analyzer = SentimentAnalyzer()
    # Print summary dataframe
    df = analyzer.analyze_multiple_reviews(sample_reviews)
    # Create and save visualization
    analyzer.visualize_sentiment(sample_reviews)