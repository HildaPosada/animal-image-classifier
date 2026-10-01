import base64
import io
import json
import os
from http.server import BaseHTTPRequestHandler
from PIL import Image, UnidentifiedImageError
from inference import predict, InferenceError

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if size <= 0 or size > 4 * 1024 * 1024:
                return self.reply(413, {'error':'Choose a smaller image (under 3 MB for web inference).'})
            data = json.loads(self.rfile.read(size))
            raw = base64.b64decode(data['image'], validate=True)
            image = Image.open(io.BytesIO(raw))
            image.load()
        except (ValueError, KeyError, TypeError, OSError, UnidentifiedImageError, Image.DecompressionBombError):
            return self.reply(400, {'error':'Upload a valid JPG or PNG image.'})
        try:
            predictions = predict(image, os.getenv('ROBOFLOW_API_KEY'), os.getenv('ROBOFLOW_PROJECT','animal-image-classifier'), os.getenv('ROBOFLOW_VERSION','1'))
        except InferenceError as exc:
            return self.reply(503, {'error':str(exc)})
        self.reply(200, {'predictions':predictions})
    def reply(self, status, body):
        self.send_response(status)
        self.send_header('Content-Type','application/json')
        self.send_header('Cache-Control','no-store')
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())
