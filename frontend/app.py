import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from PIL import Image
import numpy as np
import cv2

from model.anpr_model import detect_plate

st.title("🚗 ANPR Number Plate Detection")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        st.image(img, channels="BGR", caption="Uploaded Image")

        path = "temp.jpg"
        cv2.imwrite(path, img)

        result = detect_plate(path)

        st.write("### Result:")
        st.success(result)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")