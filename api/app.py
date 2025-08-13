from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)
model = joblib.load('models/fraud_model.pkl')
@app.route('/')
def home():
    return "✅ Real-Time Fraud Detection API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        required_fields = ['transaction_id', 'amount', 'timestamp', 'location', 'user_id']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Convert location to binary (0 = same, 1 = different)
        location_value = 1 if data['location'].lower() == 'different' else 0

        # Format input for model
        input_features = np.array([[data['amount'], location_value, data['user_id']]])

        # Predict
        prediction = model.predict(input_features)[0]
        probability = model.predict_proba(input_features)[0][1]

        result = {
            'transaction_id': data['transaction_id'],
            'is_fraud': bool(prediction),
            'confidence': round(float(probability), 2)
        }

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)