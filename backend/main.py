from fastapi import FastAPI, File, UploadFile
import shutil
import os
import sys

# 🔥 FIX PATH FOR DOCKER
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from anpr_model import detect_plate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ANPR API Running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_plate(file_path)

    os.remove(file_path)

    return {"plates": result}