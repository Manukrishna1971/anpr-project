import streamlit as st
import requests

st.title("🚗 Number Plate Recognition System")

uploaded_file = st.file_uploader("Upload Vehicle Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Detect Plate"):
        try:
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                files=files
            )

            if response.status_code == 200:
                result = response.json()
                st.success("Detected Plates:")
                st.write(result["plates"])
            else:
                st.error(f"Server Error: {response.status_code}")

        except Exception as e:
            st.error(f"Error: {e}")