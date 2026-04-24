FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir \
    fastapi uvicorn streamlit easyocr opencv-python ultralytics pillow requests torch torchvision torchaudio

EXPOSE 8000 8501

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]