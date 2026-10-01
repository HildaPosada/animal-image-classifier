"""Roboflow request and response handling, independent of the UI."""
import io
import math
import requests

class InferenceError(Exception):
    pass

def predict(image, api_key, project='yolo1-petqw', version='1'):
    if not api_key:
        raise InferenceError('Prediction service is not configured. Set ROBOFLOW_API_KEY.')
    buffer = io.BytesIO()
    image.convert('RGB').save(buffer, format='JPEG')
    try:
        response = requests.post(
            f'https://detect.roboflow.com/{project}/{version}',
            params={'api_key': api_key},
            files={'file': ('image.jpg', buffer.getvalue(), 'image/jpeg')},
            timeout=(10, 45),
        )
    except requests.Timeout:
        raise InferenceError('Prediction service timed out. Please try again.') from None
    except requests.RequestException:
        raise InferenceError('Could not reach the prediction service. Please try again.') from None
    if response.status_code in (401, 403):
        raise InferenceError('Prediction service rejected its credentials. Check the server configuration.')
    if not response.ok:
        raise InferenceError(f'Prediction service returned HTTP {response.status_code}. Please try again later.')
    try:
        body = response.json()
        predictions = body['predictions']
        if not isinstance(predictions, list):
            raise ValueError()
        cleaned = []
        for item in predictions:
            label = item['class']
            confidence = float(item['confidence'])
            if not isinstance(label, str) or not label.strip() or not math.isfinite(confidence) or not 0 <= confidence <= 1:
                raise ValueError()
            cleaned.append({'class': label, 'confidence': confidence})
    except (ValueError, KeyError, TypeError):
        raise InferenceError('Prediction service returned an unexpected response.') from None
    return sorted(cleaned, key=lambda item: item['confidence'], reverse=True)
