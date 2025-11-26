# test_sentiment.py
from sentiment_analyzer import SentimentAnalyzer

def test_analyzer():
    """Test the sentiment analyzer with various inputs"""
    analyzer = SentimentAnalyzer()

    # Test reviews
    test_cases = [
        # Clear positive
        "This is the best product I've ever bought! Amazing quality!",
        # Clear negative  
        "Horrible product. Complete waste of money. Very disappointed.",
        # Neutral/mixed
        "The product is okay. Some features are good, others not so much.",
        # Sarcastic (challenging!)
        "Oh great, it broke on the first day. Just wonderful.",
        # Complex
        "Started great but quality declined. Was happy, now frustrated."
    ]

    print("=" * 60)
    print("SENTIMENT ANALYZER TEST RESULTS")
    print("=" * 60)

    for i, review in enumerate(test_cases, 1):
        print(f"\n Test {i}: {review}")
        print("-" * 50)

        # Simple analysis
        simple = analyzer.analyze_sentiment_simple(review)
        print(f"Simple Method: {simple['sentiment']} "
              f"(Confidence: {simple['confidence']:.1f}% )")

        # Advanced analysis   
        advanced = analyzer.analyze_sentiment_advanced(review)
        print(f"Advanced Method: {advanced['sentiment']} "
              f"(Polarity: {advanced['polarity']:.3f})")

    # Visualize results
    print("\n\n📊 Creating visualization...")
    analyzer.visualize_sentiment(test_cases)

if __name__ == "__main__":
    test_analyzer()
