# test_classifier.py
from classifier import ImageClassifier
import os

def main():
    print("="*60)
    print("🖼️  IMAGE CLASSIFIER TEST")
    print("="*60)
    
    classifier = ImageClassifier()
    
    # Explain the process 
    classifier.explain_process()
    
    # Menu
    while True:
        print("\n" + "="*60)
        print("TESTING OPTIONS")
        print("="*60)
        print("1. Classify images from test_images folder")
        print("2. Use webcam for real-time classification")
        print("3. Start web interface")
        print("4. Learn about computer vision challenges")
        print("5. Exit")
        
        choice = input("\nChoice (1-5): ")
        
        if choice == '1':
            # Test with images in folder 
            test_folder = 'test_images'
            if os.path.exists(test_folder):
                images = [f for f in os.listdir(test_folder)  
                         if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                
                if images:
                    for img in images:
                        path = os.path.join(test_folder, img)
                        print(f"\n🖼️ Classifying: {img}")
                        classifier.visualize_prediction(path)
                else:
                    print("No images found in test_images folder!")
            else:
                print("Create a 'test_images' folder and add images to test!")
        
        elif choice == '2':
            classifier.classify_from_webcam()
        
        elif choice == '3':
            print("\n🌐 Starting web server...")
            print("Run: python web_interface.py")
            print("Then visit: http://localhost:5000")
        
        elif choice == '4':
            print("\n📚 COMPUTER VISION CHALLENGES")
            print("-" * 40)
            print("1. LIGHTING: Same object looks different in shadow vs bright light")
            print("2. ANGLE: Front view vs side view of face")
            print("3. OCCLUSION: When objects partially block each other")
            print("4. SCALE: Same object at different distances")
            print("5. BACKGROUND: Busy backgrounds make detection harder")
            print("6. VARIATIONS: Every apple looks slightly different!")
            
        elif choice == '5':
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()
