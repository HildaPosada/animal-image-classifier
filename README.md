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

<table>
  <tr>
    <td>🦁 Lion</td>
    <td>🐯 Tiger</td>
  </tr>
  <tr>
    <td>🐘 Elephant</td>
    <td>🦓 Zebra</td>
  </tr>
  <tr>
    <td>🦒 Giraffe</td>
    <td>🦘 Kangaroo</td>
  </tr>
  <tr>
    <td>🐼 Panda</td>
    <td>🐒 Monkey</td>
  </tr>
  <tr>
    <td>🐻 Bear</td>
    <td>🦩 Flamingo</td>
  </tr>
</table>

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
│   ├── app.py
│   ├── utils.py
│   └── demo.png  (optional screenshot)
├── models/       (optional)
├── notebooks/    (optional)
├── requirements.txt
├── README.md
└── .gitignore
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
```
🔗 Roboflow Dataset

This model was trained on the YOLO1 - Pet Dataset by Aysha Salman on Roboflow Universe.
[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-success?style=flat&logo=streamlit)](https://share.streamlit.io/your-app-link)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue)](http://localhost:5000)
[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/)

## 📸 Demo Screenshot

<img src="app/demo.png" width="700"/>


