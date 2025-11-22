# Computer Vision Image Classifier 
 
## Project Overview 
This project implements image classification using computer vision concepts from Chapter 
24. The AI can recognize objects in images using a neural network trained with Teachable 
Machine. 
 
## My Classification Task 
**Classes:** Sad, Happy, Surprised
**Training Images:** [50 plus] images per class 
**Accuracy:** 71
## How to Run 
1. **Install Requirements** 
```bash 
pip install -r requirements.txt 
``` 
2. **Test the Classifier** 
```bash 
python test_classifier.py 
``` 
3. **Web Interface** 
```bash 
python web_interface.py 
``` 
Visit http://localhost:5000 
## How Computer Vision Works 
### Image as Numbers 
Every image is a grid of pixels. Each pixel has RGB values (0-255 for Red, Green, Blue). 
### Feature Detection 
The neural network learns to detect: - **Edges**: Where colors change sharply - **Shapes**: Combinations of edges - **Patterns**: Repeated features - **Objects**: Complex combinations 
### My Model's Process 
1. Resize image to 224x224 pixels 
2. Normalize pixel values 
3. Pass through neural network 
4. Get probability for each class 
5. Return highest probability as prediction 
## Challenges I Encountered 
I struggled to install and configure Conda correctly. This slowed down environment setup and package management.
## Real-World Applications 
1. **Medical**:Supporting mental health assessments by tracking emotional states
2. **Security**: Surveillance systems can detect unusual emotional states (fear, distress, anger)
3. **Retail**: Supporting mental health assessments by tracking emotional states
## Ethical Considerations 
Users should be informed how their facial data is processed and stored
Training data should include diverse faces to avoid skewed predictions
## What I Learned 
Why diverse training data (different faces, lighting, angles) is critical for generalization
Practical limits of small models