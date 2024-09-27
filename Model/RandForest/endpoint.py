import pickle
import numpy as np
from flask import Flask, request, jsonify

# Booting up model
filename = "..\Model\GradesRF.sav"
model = pickle.load(open(filename, "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.json

    # Get data from request, set to np.nan if not present
    try:
        studytime = data.get('studytime', np.nan)
        failures = data.get('failures', np.nan)
        absences = data.get('absences', np.nan)
        
        # Convert schoolsup and paid from bool to integer, set to np.nan if empty
        schoolsup = int(data['schoolsup']) if isinstance(data.get('schoolsup'), bool) else (data.get('schoolsup', np.nan))
        paid = int(data['paid']) if isinstance(data.get('paid'), bool) else (data.get('paid', np.nan))
        
        health = data.get('health', np.nan)
        G1 = data.get('G1', np.nan)
        G2 = data.get('G2', np.nan)
        G3 = data.get('G3', np.nan)
        
        # Final Input Data
        input_data = np.array([[studytime, failures, absences, schoolsup, paid, health, G1, G2, G3]])
        
        # Predict
        pred = model.predict(input_data)

        # Return prediction
        return jsonify({'prediction': pred[0]})
    
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)