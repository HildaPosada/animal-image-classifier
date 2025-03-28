# 🐯 Animal Image Classifier

A machine learning project that classifies images of 10 exotic animals using a deep learning model. The model is deployed via an interactive Streamlit app for real-time image classification.

## 🔍 Project Overview
This project demonstrates the full ML pipeline:
- Image classification of exotic animals using a CNN model (ResNet34 via Roboflow)
- Model training with 47,000+ annotated images
- Streamlit app for easy user interaction
- (Optional) MLflow integration for experiment tracking
- GitHub for version control and open collaboration

## 🐾 Animal Classes
The model classifies the following exotic animals:
- 🦁 Lion
- 🐯 Tiger
- 🐘 Elephant
- 🦓 Zebra
- 🦒 Giraffe
- 🦘 Kangaroo
- 🐼 Panda
- 🐒 Monkey
- 🐻 Bear
- 🦩 Flamingo

## 🧰 Tools & Technologies
- **Python**
- **Roboflow** – dataset management & model training
- **PyTorch/TensorFlow** – model backend
- **Streamlit** – frontend interface
- **MLflow** – experiment tracking (optional)
- **GitHub** – version control

## 🗂️ Project Structure
```
animal-image-classifier/
├── app/
│ ├── app.py # Main Streamlit app
│ ├── utils.py # Helper functions for inference
│     └── data/ # (Optional) Local test images
├── models/ # Trained model (e.g., .pt, .h5, .onnx)
├── notebooks/
│   └── training.ipynb # Training notebook
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore file
├── LICENSE
└── README.md
```

## 🚀 How to Run the App
```bash
# Step 1: Clone the repo
git clone https://github.com/your-username/animal-image-classifier.git
cd animal-image-classifier

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
streamlit run app/app.py

🔗 Roboflow Dataset

This model was trained on the YOLO1 - Pet Dataset by Aysha Salman on Roboflow Universe.
