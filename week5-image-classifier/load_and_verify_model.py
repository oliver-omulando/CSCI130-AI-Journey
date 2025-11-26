"""Load and verify Keras model and labels placed in week5-image-classifier/model/"""
from pathlib import Path
import sys

MODEL = Path(__file__).parent / 'model' / 'keras_model.h5'
LABELS = Path(__file__).parent / 'model' / 'labels.txt'

if not MODEL.exists():
    print(f"Model file not found: {MODEL}")
    sys.exit(2)

print(f"Loading model from: {MODEL}")
try:
    import tensorflow as tf
except Exception as e:
    print("Failed to import tensorflow:", e)
    sys.exit(3)

model = tf.keras.models.load_model(str(MODEL), compile=False)
print("Model loaded. Summary:")
try:
    model.summary()
except Exception:
    print(repr(model))

if LABELS.exists():
    with LABELS.open('r', encoding='utf-8') as f:
        labels = [l.strip() for l in f if l.strip()]
    print(f"Loaded {len(labels)} labels. First 20 (or fewer):")
    for i, l in enumerate(labels[:20], 1):
        print(f" {i}. {l}")
else:
    print(f"Labels file not found: {LABELS}")

print("Verification complete.")
