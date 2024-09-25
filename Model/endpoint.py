import pickle
import flask

filename = "Model/GradePredictor.sav"
model = pickle.load(open(filename, "rb"))