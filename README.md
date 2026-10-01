# Animal Image Classifier

A Streamlit interface that submits uploaded images to a configured Roboflow inference endpoint and displays its predictions.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Set `ROBOFLOW_API_KEY` in the deployment's secret/environment settings. Optional `ROBOFLOW_PROJECT` and `ROBOFLOW_VERSION` select the model; defaults are `animal-image-classifier` and `1`. Never commit the key.

The app validates image uploads, uses request timeouts, distinguishes service failures from empty detections, and displays the highest-confidence prediction first. It does not train a model locally.

## What is verified

Response handling is tested with controlled API responses. These tests do not establish model accuracy. A real inference run requires valid deployment credentials and a reachable model.

The repository does not contain model weights, a training dataset, or recorded evaluation results. The empty training notebook is not evidence of training. Architecture, dataset size, and supported classes must be confirmed from the actual Roboflow project before being claimed.

A model can misclassify dogs, unfamiliar species, and non-animal images. A high confidence score is not a guarantee of correctness. Evaluate known positive images and out-of-distribution inputs before making accuracy claims.

## Web demo deployment

The `web/` directory contains the static interface and Python prediction endpoint. Set Vercel's Root Directory to `web`, Framework Preset to Other, and store `ROBOFLOW_API_KEY` as a secret for Production and Preview. The browser submits images to `/api/predict`; the key stays on the server. Uploads are limited to 3 MB. Predictions are requested from Roboflow, not generated randomly.

Roboflow identifies the hosted model as ResNet34 Classification and reports 77.6% validation accuracy. This is the provider's evaluation, not an independent accuracy measurement from this repository.
