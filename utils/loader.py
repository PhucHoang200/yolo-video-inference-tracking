from ultralytics import YOLO
import os

MODEL_PATH = os.path.join("models", "best.pt")

def load_model():
    model = YOLO(MODEL_PATH)
    return model
