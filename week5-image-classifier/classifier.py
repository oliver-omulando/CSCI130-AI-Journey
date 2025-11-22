import os
from pathlib import Path
from typing import List, Tuple

import numpy as np
from PIL import Image

try:
    import tensorflow as tf
    from tensorflow import keras
except Exception:
    tf = None
    keras = None


class ImageClassifier:
    """Simple image classifier wrapper used by the Week 5 project.

    - Loads a Keras model from `model/` by default
    - Loads labels from `model/labels.txt` (supports lines like "0 happy")
    """

    def __init__(self, model_path: str = 'model/keras_model.keras', labels_path: str = 'model/labels.txt'):
        self.model_path = Path(model_path)
        self.labels_path = Path(labels_path)
        self.model = None
        self.labels = self._load_labels()
        self.image_size = (224, 224)

        # lazy model loading
        if self.model_path.exists():
            try:
                self._load_model()
            except Exception as e:
                print(f'Warning: failed to load model at {self.model_path}: {e}')

    def _load_labels(self) -> List[str]:
        if not self.labels_path.exists():
            return ['happy', 'sad', 'suprised']

        labels = []
        with self.labels_path.open('r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if parts[0].isdigit() and len(parts) > 1:
                    labels.append(' '.join(parts[1:]))
                else:
                    labels.append(line)
        return labels

    def _load_model(self):
        if keras is None:
            raise RuntimeError('TensorFlow / Keras is not available in this Python environment')
        mp = self.model_path
        if not mp.exists():
            alt = mp.with_suffix('.h5')
            if alt.exists():
                mp = alt
            else:
                raise FileNotFoundError(f'Model not found: {self.model_path}')

        self.model = keras.models.load_model(str(mp), compile=False)

    def preprocess_image(self, image_path: str) -> np.ndarray:
        img = Image.open(image_path).convert('RGB')
        img = img.resize(self.image_size)
        arr = np.array(img).astype('float32') / 255.0
        return np.expand_dims(arr, axis=0)

    def classify_image(self, image_path: str) -> Tuple[List[dict], Image.Image]:
        if self.model is None:
            self._load_model()

        arr = self.preprocess_image(image_path)
        probs = self.model.predict(arr, verbose=0)[0]

        results = []
        for i, p in enumerate(probs):
            lbl = self.labels[i] if i < len(self.labels) else str(i)
            results.append({'class': lbl, 'confidence': float(p * 100)})

        results.sort(key=lambda x: x['confidence'], reverse=True)

        pil_img = Image.open(image_path).convert('RGB')
        return results, pil_img

    def visualize_prediction(self, image_path: str, save_path: str = 'prediction_result.png') -> dict:
        import matplotlib.pyplot as plt

        results, img = self.classify_image(image_path)
        top3 = results[:3]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        ax1.imshow(img)
        ax1.axis('off')
        ax1.set_title('Input Image')

        classes = [r['class'] for r in top3]
        confidences = [r['confidence'] for r in top3]
        ax2.barh(classes, confidences, color='#667eea')
        ax2.set_xlim(0, 100)
        ax2.set_xlabel('Confidence (%)')
        for i, c in enumerate(confidences):
            ax2.text(c + 1, i, f'{c:.1f}%')

        plt.tight_layout()
        plt.savefig(save_path)
        plt.close(fig)

        return results[0] if results else {}

    def classify_from_webcam(self):
        import cv2

        if self.model is None:
            self._load_model()

        cap = cv2.VideoCapture(0)
        print('Press q to quit, c to capture and classify')
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Webcam', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            if key == ord('c'):
                tmp = 'webcam_capture.jpg'
                cv2.imwrite(tmp, frame)
                results, _ = self.classify_image(tmp)
                print('Top predictions:')
                for r in results[:3]:
                    print(f"{r['class']}: {r['confidence']:.2f}%")

        cap.release()
        cv2.destroyAllWindows()

    def explain_process(self):
        print('\nHOW COMPUTER VISION WORKS')
        print('-' * 40)
        print('1. Capture image as pixels (RGB)')
        print('2. Resize and normalize to model input')
        print('3. Pass through neural network')
        print('4. Output probabilities for each class')
