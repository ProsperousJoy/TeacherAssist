import pickle
import numpy as np
from flask import Flask, request

filename = "Model/GradesRF.sav"
model = pickle.load(open(filename, "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    print("adhuadha")

input_data = np.array([[5, 0, 3, 1, 1, 1, 90, 65, np.nan]])

pred = model.predict(input_data)

print(pred)
