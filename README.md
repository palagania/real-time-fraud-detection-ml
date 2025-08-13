# Real-Time Fraud Detection using Machine Learning

This project implements a real-time fraud detection system using machine learning and streaming data technologies. It simulates transaction streams, detects anomalies, and predicts fraudulent activities using trained ML models.

## 🔧 Tech Stack

- **Python**
- **Apache Kafka** – for streaming data
- **Apache Spark** – for real-time processing
- **Flask API** – to expose ML predictions
- **PostgreSQL** – for storing transaction data
- **Docker** & **Docker Compose**

## 📁 Project Structure

real-time-fraud-detection-ml/
│
├── api/ # Flask API to serve the ML model
├── db/ # SQL scripts and database setup
├── kafka/ # Kafka producer/consumer setup
├── spark/ # Spark streaming job
├── docker-compose.yml # To run everything together
└── README.md


## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/palagania/real-time-fraud-detection-ml.git
   cd real-time-fraud-detection-ml

Run with Docker Compose
  docker-compose up --build


Test the API
Use cURL or Postman:

curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"transaction_id": "TX123", "amount": 500, "timestamp": "2025-08-12T10:30:00Z", "location": "NY", "user_id": 42}'

✅ Features
Live transaction simulation

Fraud probability scoring
Real-time fraud classification
Full-stack deployment using Docker

👤 Author
Abhinash Palagani – GitHub

📜 License
This project is open-source and available under the MIT License.


---

### ✅ What to Do Next

1. **Edit your README.md** file:
   - Go to the [README.md on GitHub](https://github.com/palagania/real-time-fraud-detection-ml/blob/main/README.md)
   - Click the **pencil icon** (✏️) to edit.
   - Paste the markdown content above.
   - Scroll down and click **"Commit changes"**.





