import pickle
import numpy as np

filename = "Model/GradesRF.sav"
model = pickle.load(open(filename, "rb"))

input_data = np.array([[5, 0, 3, 1, 1, 1, 90, 65, np.nan]])

pred = model.predict(input_data)

print(pred)
