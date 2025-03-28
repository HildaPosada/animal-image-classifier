import streamlit as st
import requests
from PIL import Image
import io
import os
import time

# --- Config ---
st.set_page_config(page_title="🐾 Animal Classifier", layout="centered")

# --- Title ---
st.markdown("<h1 style='text-align: center;'>🐯 Animal Image Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload an exotic animal image and get predictions with confidence 📸</p>", unsafe_allow_html=True)

# --- Upload Image ---
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# --- Roboflow Config ---
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
PROJECT_NAME = "yolo1-petqw"
PROJECT_VERSION = "1"

def predict_with_roboflow(image):
    api_url = f"https://detect.roboflow.com/{PROJECT_NAME}/{PROJECT_VERSION}?api_key={ROBOFLOW_API_KEY}"
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    response = requests.post(api_url, files={"file": img_bytes})
    return response.json() if response.status_code == 200 else None

# --- Show Image & Predict ---
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Image", use_column_width=True)

    with st.spinner("🧠 Thinking..."):
        result = predict_with_roboflow(image)
        time.sleep(1)

    if result and result.get("predictions"):
        pred = result["predictions"][0]
        label = pred["class"]
        confidence = float(pred["confidence"]) * 100

        st.markdown(f"### 🐾 Prediction: `{label}`")
        st.progress(int(confidence))
        st.success(f"Confidence: {confidence:.2f}%")
    else:
        st.warning("❌ No animal detected. Try a clearer or different image.")
