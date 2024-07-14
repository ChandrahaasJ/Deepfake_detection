
import io
import os
import cv2
import numpy as np
from flask import Flask, request, jsonify, send_file
from patchify import patchify
from werkzeug.utils import secure_filename
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB0
import tensorflow as tf
from tqdm import tqdm
from controller.controlFunctions import extractaudio,extractframes,cleardir

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return 'Hello World!'

# def build_model(num_classes):
#     IMG_SIZE = 224
#     inputs = layers.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
#     x = inputs
#     model = EfficientNetB0(include_top=False, input_tensor=x, weights="imagenet")

#     # Freeze the pretrained weights
#     model.trainable = False

#     # Rebuild top
#     x = layers.GlobalAveragePooling2D(name="avg_pool")(model.output)
#     x = layers.BatchNormalization()(x)

#     top_dropout_rate = 0.2
#     x = layers.Dropout(top_dropout_rate, name="top_dropout")(x)
#     outputs = layers.Dense(num_classes, activation="softmax", name="pred")(x)

#     # Compile
#     model = tf.keras.Model(inputs, outputs, name="EfficientNet")
#     optimizer = tf.keras.optimizers.Adam(learning_rate=1e-2)
#     model.compile(
#         optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"]
#     )
#     return model


# # Load the model once at startup
# NUM_CLASSES = 2
# MODEL_PATH = "Efficient_Net_Final.weights.h5"
# model = build_model(num_classes=NUM_CLASSES)
# model.load_weights(MODEL_PATH)
# class_labels = ['fake', 'real']


@app.route('/audio/extractor',methods=['POST'])
def aud():
    if 'video' not in request.files:
        return jsonify({'error':"No video was sent"}),400
    file=request.files['video']
    if file=='':
        return jsonify({'error':"no file present"}),400
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        cleardir('D:/Projects/Deepfake_detection/Server/uploads')
        file.save(file_path)
        audiopath=extractaudio(file_path)
        return jsonify({"audio-path":audiopath})



# @app.route('/videosplitter', methods=['POST'])
# def videosplitter():
#     if 'video' not in request.files:
#         return jsonify({'error': 'No video part in the request'}), 400
#     file = request.files['video']
#     if file.filename == '':
#         return jsonify({'error': 'No selected video file'}), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         output_video_path = process_video_dl(file_path)

#         return send_file(output_video_path, as_attachment=True)

#     return jsonify({'error': 'File type not allowed'}), 400


# @app.route('/magic/endpoint',methods=['GET','POST'])
# def magicep():
#     if request.method=='POST':
#         image_data = request.files['image']

#         # Convert binary data to PIL Image
#         image = Image.open(image_data).resize((224, 224))

#         path = "Efficient_Net_Final.weights.h5"

#         NUM_CLASSES = 3

#         model = build_model(num_classes=NUM_CLASSES)

#         model.load_weights(path)

if __name__=='__main__':
    app.run("0.0.0.0",debug=True)
