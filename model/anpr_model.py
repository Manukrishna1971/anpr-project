from ultralytics import YOLO
import easyocr
import cv2
import re

# YOLO model (optional)
model = YOLO("yolov8n.pt")

# GPU enabled OCR
reader = easyocr.Reader(['en'], gpu=True)

def clean_text(text):
    return re.sub(r'[^A-Z0-9]', '', text.upper())

def detect_plate(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return ["Error loading image"]

    # Resize for speed
    img = cv2.resize(img, (640, 480))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    results = reader.readtext(gray, detail=1)

    best_text = ""

    for (_, text, prob) in results:
        if prob > 0.3:
            cleaned = clean_text(text)
            if len(cleaned) > len(best_text):
                best_text = cleaned

    if best_text:
        return [best_text]

    return ["No plate detected"]