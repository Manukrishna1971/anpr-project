import cv2
import easyocr

# Initialize OCR reader
reader = easyocr.Reader(['en'])

def detect_plate(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return ["Error: Image not found"]

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OCR detection
    results = reader.readtext(gray)

    plates = []
    for (bbox, text, prob) in results:
        if prob > 0.3:
            plates.append(text)

    return plates