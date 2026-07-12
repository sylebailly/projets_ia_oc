import json
import os
import joblib
import keras
import tensorflow as tf
from azureml.core.model import Model
from azureml.core import Workspace
import numpy as np
import pickle
from PIL import Image


def init():
    global model
    model_path = (Model.get_model_path('segim'))
    model = keras.models.load_model(model_path, compile=False)


def run(raw_data):

    image = pickle.loads(json.loads(raw_data).encode('latin-1'))
    
    dims = image.shape
    image_source = Image.fromarray(image)
    image_source_rsz = image_source.resize((224, 224))
    image_rsz = np.array(image_source_rsz)
    
    x = np.expand_dims(image_rsz, axis=0)
    x = tf.keras.applications.resnet50.preprocess_input(x)

    z = model.predict(x)
    
    z = np.squeeze(z)
    z = z.reshape(224, 224, 8)
    y = np.argmax(z, axis=2)

    color_map = {
        '0': [0, 0, 0],
        '1': [153, 153, 0],
        '2': [255, 204, 204],
        '3': [255, 0, 127],
        '4': [0, 255, 0],
        '5': [0, 204, 204],
        '6': [255, 0, 0],
        '7': [0, 0, 255]
    }
    
    img_color = image_rsz.copy()   
    for i in range(224):
        for j in range(224):
            img_color[i, j] = color_map[str(y[i, j])]
            
    img_color_pred = Image.fromarray(img_color)
    img_color_rsz = img_color_pred.resize((dims[1], dims[0]))

    serialized_as_json = json.dumps(pickle.dumps(img_color_rsz).decode('latin-1'))

    return serialized_as_json

