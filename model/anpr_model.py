from ultralytics import YOLO
import cv2
import easyocr

model = YOLO("yolov8n.pt")  # still using base model
reader = easyocr.Reader(['en'])

def detect_plate(image_path):
    try:
        img = cv2.imread(image_path)

        if img is None:
            return "❌ Image not loaded"

        # Instead of YOLO (since not trained), scan full image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        results = reader.readtext(gray)

        texts = []

        for (_, text, prob) in results:
            if prob > 0.3:
                texts.append(text)

        if len(texts) == 0:
            return "⚠️ No plate text found"

        return "Detected: " + max(texts, key=len)

    except Exception as e:
        return f"❌ Error: {str(e)}"