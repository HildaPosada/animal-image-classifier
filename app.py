import streamlit as st
import requests
from PIL import Image
import io
import os

# Title
st.set_page_config(page_title="Animal Image Classifier 🐾", layout="centered")
st.title("🐯 Animal Image Classifier")
st.markdown("Upload an image of an exotic animal, and I'll tell you what it is!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Load your Roboflow API key (set this as an environment variable for security)
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")  # or replace with 'your_api_key_here'
PROJECT_NAME = "yolo1-petqw"  # from your dataset URL
PROJECT_VERSION = "1"         # version you trained

# Predict with Roboflow
def predict_with_roboflow(image):
    api_url = f"https://detect.roboflow.com/{PROJECT_NAME}/{PROJECT_VERSION}?api_key={ROBOFLOW_API_KEY}"

    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    response = requests.post(api_url, files={"file": img_bytes})
    
    if response.status_code == 200:
        prediction = response.json()
        return prediction
    else:
        st.error("Prediction failed. Check API key or image.")
        return None

# Main logic
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    with st.spinner("Classifying..."):
        prediction = predict_with_roboflow(image)

    if prediction:
        try:
            top_prediction = prediction["predictions"][0]
            label = top_prediction["class"]
            confidence = float(top_prediction["confidence"]) * 100
            st.success(f"Prediction: **{label}** ({confidence:.2f}% confidence)")
        except IndexError:
            st.warning("No animal detected. Try another image.")

