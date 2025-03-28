# 🐯 Animal-image-classifier

A machine learning project that classifies images of 10 exotic animals using a deep learning model and deploys it through a Streamlit app.

## 🔍 Project Overview
This project:
- Uses image classification to recognize different exotic animals
- Trains a CNN model (e.g., MobileNet, ResNet)
- Deploys the model in an interactive Streamlit app

## 🐾 Animal Classes
The model is trained to recognize the following animals:
- lion 🦁
- tiger 🐯
- elephant 🐘
- zebra 🦓
- giraffe 🦒
- kangaroo 🦘
- panda 🐼
- monkey 🐒
- bear 🐻
- flamingo 🦩

## 🧠 Tools & Tech Stack
- Python
- TensorFlow or PyTorch
- Roboflow (for dataset management)
- Streamlit (for deployment)
- MLflow (for experiment tracking, optional)
- GitHub (for version control)

## 🗂️ Project Structure
```
animal-image-classifier/
├── app/ # Streamlit app
│  ├── app.py # Main Streamlit script
│     └── utils.py # Helper functions for loading/preprocessing
│  ├── data/ # (Optional) Sample or test data
│  ├── models/ # Trained model files (e.g., model.h5 or .pt)
│  ├── notebooks/
│     └── training.ipynb # Jupyter notebook for training & EDA
│  ├── .gitignore # Files to ignore in Git
├── LICENSE # Project license
├── README.md # This file
└── requirements.txt # Python dependencies
```

## 🚀 How to Run the App
```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the Streamlit app
streamlit run app/app.py
