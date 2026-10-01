# Animal Image Classifier

A Streamlit interface that submits uploaded images to a configured Roboflow inference endpoint and displays its predictions.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Set `ROBOFLOW_API_KEY` in the deployment's secret/environment settings. Optional `ROBOFLOW_PROJECT` and `ROBOFLOW_VERSION` select the model; defaults are `yolo1-petqw` and `1`. Never commit the key.

The app validates image uploads, uses request timeouts, distinguishes service failures from empty detections, and displays the highest-confidence prediction first. It does not train a model locally.

## What is verified

Response handling is tested with controlled API responses. These tests do not establish model accuracy. A real inference run requires valid deployment credentials and a reachable model.

The repository does not contain model weights, a training dataset, or recorded evaluation results. The empty training notebook is not evidence of training. Architecture, dataset size, and supported classes must be confirmed from the actual Roboflow project before being claimed.

A model can misclassify dogs, unfamiliar species, and non-animal images. A high confidence score is not a guarantee of correctness. Evaluate known positive images and out-of-distribution inputs before making accuracy claims.

The Vercel page at `animal-demo-flax.vercel.app` is a separate interface; its inspected implementation used preset sample scores and random labels for uploads. It should not be presented as real inference until connected to a model.
