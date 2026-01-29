from flask import Flask, render_template, request, jsonify
import cv2, base64
import numpy as np
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import face_recognition
import os

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["5/minute"])

known_encodings = []

def load_faces():
    for f in os.listdir("known_faces"):
        img = face_recognition.load_image_file(f"known_faces/{f}")
        enc = face_recognition.face_encodings(img)
        if enc:
            known_encodings.append(enc[0])

load_faces()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
@limiter.limit("5/minute")
def login():
    image_data = request.json["image"]
    frame = cv2.imdecode(
        np.frombuffer(base64.b64decode(image_data.split(",")[1]), np.uint8),
        cv2.IMREAD_COLOR
    )

    rgb = frame[:, :, ::-1]
    encodings = face_recognition.face_encodings(rgb)

    for enc in encodings:
        if True in face_recognition.compare_faces(known_encodings, enc, 0.5):
            return jsonify({"status": "success"})

    return jsonify({"status": "failed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
