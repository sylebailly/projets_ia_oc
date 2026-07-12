import json
import os
import joblib


def init():
    global model
    model = joblib.load(os.getenv("AZUREML_MODEL_DIR") + "/model/model.pkl")
  

def run(raw_data):
    data = json.loads(raw_data)["data"]
    # make prediction
    y_hat = model.predict(data)
    # you can return any data type as long as it is JSON-serializable
    return y_hat.tolist()


