# spam_detector.py 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score, confusion_matrix 
import matplotlib.pyplot as plt 
 
class SpamDetector: 
    """ 
    A simple spam detector using machine learning 
    Demonstrates concepts from Chapter 18 
    """ 
     
    def __init__(self): 
        self.model = DecisionTreeClassifier(max_depth=3) 
        self.is_trained = False 
     
    def load_data(self, filepath): 
        """Load email data from CSV""" 
        self.data = pd.read_csv(filepath) 
        print(f"Loaded {len(self.data)} emails") 
        return self.data 
     
    def prepare_features(self): 
        """ 
        Separate features (X) from labels (y) 
        Features: what the model learns from 
        Labels: what we're trying to predict 
        """ 
        # Features (things we measure about emails) 
        feature_columns = ['word_count', 'exclamations', 'money_words', 'all_caps'] 
        self.X = self.data[feature_columns] 
         
        # Labels (spam or not spam) 
        self.y = self.data['is_spam'] 
         
        print("\n📊 Feature Statistics:") 
        print("-" * 40) 
        print("Average values by email type:") 
        print(self.data.groupby('is_spam')[feature_columns].mean()) 
         
    def split_data(self): 
        """ 
        Split into training and testing sets 
        This prevents overfitting! 
        """ 
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split( 
            self.X, self.y, test_size=0.3, random_state=42 
        ) 
         
        print(f"\n📚 Training set: {len(self.X_train)} emails") 
        print(f"🧪 Testing set: {len(self.X_test)} emails") 
     
    def train(self): 
        """Train the model on training data""" 
        print("\n🤖 Training the spam detector...") 
        self.model.fit(self.X_train, self.y_train) 
        self.is_trained = True 
         
        # Check training accuracy 
        train_pred = self.model.predict(self.X_train) 
        train_accuracy = accuracy_score(self.y_train, train_pred) 
        print(f"Training accuracy: {train_accuracy:.1%}") 
     
    def test(self): 
        """Test the model on unseen data""" 
        if not self.is_trained: 
            print("Model not trained yet!") 
            return 
         
        print("\n🧪 Testing on new emails...") 
        self.y_pred = self.model.predict(self.X_test) 
        test_accuracy = accuracy_score(self.y_test, self.y_pred) 
        print(f"Testing accuracy: {test_accuracy:.1%}") 
         
        # Show confusion matrix 
        cm = confusion_matrix(self.y_test, self.y_pred) 
        print("\nConfusion Matrix:") 
        print("                Predicted") 
        print("              Normal  Spam") 
        print(f"Actual Normal    {cm[0,0]:3d}   {cm[0,1]:3d}") 
        print(f"Actual Spam      {cm[1,0]:3d}   {cm[1,1]:3d}") 
         
        return test_accuracy 
     
    def predict_email(self, word_count, exclamations, money_words, all_caps): 
        """Predict if a single email is spam""" 
        if not self.is_trained: 
            print("Model not trained yet!") 
            return 
         
        features = [[word_count, exclamations, money_words, all_caps]] 
        prediction = self.model.predict(features)[0] 
        probability = self.model.predict_proba(features)[0] 
         
        result = "SPAM" if prediction == 1 else "NORMAL" 
        confidence = max(probability) * 100 
         
        print(f"\n📧 Email Analysis:") 
        print(f"  Word count: {word_count}") 
        print(f"  Exclamation marks: {exclamations}") 
        print(f"  Money-related words: {money_words}") 
        print(f"  ALL CAPS words: {all_caps}") 
        print(f"\n🎯 Prediction: {result}") 
        print(f"🔍 Confidence: {confidence:.1f}%") 
         
        return prediction 
     
    def visualize_data(self): 
        """Create visualizations to understand the data""" 
        fig, axes = plt.subplots(2, 2, figsize=(12, 10)) 
         
        # Plot 1: Word count distribution 
        axes[0,0].hist([self.data[self.data['is_spam']==0]['word_count'], 
                       self.data[self.data['is_spam']==1]['word_count']], 
                      label=['Normal', 'Spam'], alpha=0.7, bins=10) 
        axes[0,0].set_xlabel('Word Count') 
        axes[0,0].set_ylabel('Number of Emails') 
        axes[0,0].set_title('Word Count Distribution') 
        axes[0,0].legend() 
         
        # Plot 2: Exclamation marks 
        axes[0,1].bar(['Normal', 'Spam'], 
                     [self.data[self.data['is_spam']==0]['exclamations'].mean(), 
                      self.data[self.data['is_spam']==1]['exclamations'].mean()]) 
        axes[0,1].set_ylabel('Average Exclamation Marks') 
        axes[0,1].set_title('Exclamation Usage') 
         
        # Plot 3: Money words 
        axes[1,0].bar(['Normal', 'Spam'], 
                     [self.data[self.data['is_spam']==0]['money_words'].mean(), 
                      self.data[self.data['is_spam']==1]['money_words'].mean()]) 
        axes[1,0].set_ylabel('Average Money Words') 
        axes[1,0].set_title('Money Word Usage') 
         
        # Plot 4: Feature importance 
        if self.is_trained: 
            importance = self.model.feature_importances_ 
            features = ['Word Count', 'Exclamations', 'Money Words', 'All Caps'] 
            axes[1,1].bar(features, importance) 
            axes[1,1].set_ylabel('Importance') 
            axes[1,1].set_title('What the Model Learned is Important') 
            axes[1,1].tick_params(axis='x', rotation=45) 
         
        plt.tight_layout() 
        plt.savefig('spam_analysis.png') 
        plt.show() 
        print("\n📊 Saved visualization as 'spam_analysis.png'")


def main(): 
    """Main program with interactive menu""" 
    print("="*50) 
    print("🚫 SPAM EMAIL DETECTOR") 
    print("Machine Learning in Action!") 
    print("="*50) 
     
    detector = SpamDetector() 
     
    # First, create the data if it doesn't exist 
    import os 
    if not os.path.exists('data/email_data.csv'): 
        print("\n📝 Creating email dataset...") 
        os.makedirs('data', exist_ok=True) 
        from prepare_data import create_sample_emails 
        data = create_sample_emails() 
        data.to_csv('data/email_data.csv', index=False) 
     
    # Load and prepare data 
    detector.load_data('data/email_data.csv') 
    detector.prepare_features() 
    detector.split_data() 
     
    # Train the model 
    detector.train() 
    detector.test() 
     
    # Visualize 
    print("\n📊 Creating visualizations...") 
    detector.visualize_data() 
     
    # Interactive testing 
    while True: 
        print("\n" + "="*50) 
        print("TEST THE SPAM DETECTOR") 
        print("="*50) 
        print("1. Test a custom email") 
        print("2. Test example spam email") 
        print("3. Test example normal email") 
        print("4. Show model performance") 
        print("5. Learn about overfitting") 
        print("6. Exit") 
         
        choice = input("\nChoice (1-6): ") 
         
        if choice == '1': 
            print("\nDescribe your email:") 
            try: 
                words = int(input("Approximate word count: ")) 
                exclaim = int(input("Number of exclamation marks: ")) 
                money = int(input("Money-related words (free, cash, win, etc.): ")) 
                caps = int(input("Words in ALL CAPS: ")) 
                detector.predict_email(words, exclaim, money, caps) 
            except ValueError: 
                print("Please enter numbers only!") 
         
        elif choice == '2': 
            print("\nTesting spam email: 'WIN FREE CASH NOW!!!'") 
            detector.predict_email(30, 3, 4, 3) 
         
        elif choice == '3': 
            print("\nTesting normal email: 'Meeting tomorrow at 2pm'") 
            detector.predict_email(100, 0, 0, 0) 
         
        elif choice == '4': 
            detector.test() 
         
        elif choice == '5': 
            print("\n📚 ABOUT OVERFITTING") 
            print("-" * 40) 
            print("Overfitting is when your model:") 
            print("• Memorizes the training data perfectly") 
            print("• But fails on new, unseen data") 
            print("\nIt's like a student who memorizes answers") 
            print("but doesn't understand the concepts!") 
            print("\nWe prevent it by:") 
            print("• Using separate test data") 
            print("• Keeping our model simple") 
            print("• Having enough diverse training examples") 
         
        elif choice == '6': 
            print("\nThanks for using Spam Detector!") 
            break 
 
if __name__ == "__main__": 
    main()       