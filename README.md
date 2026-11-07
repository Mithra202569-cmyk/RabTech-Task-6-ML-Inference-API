# Real-Time Sentiment Analysis API

## Project Overview
This project implements a real-time Machine Learning REST API using FastAPI. It uses a trained sentiment analysis model to classify movie reviews as Positive or Negative.

## Technologies Used
- Python
- TensorFlow
- FastAPI
- Uvicorn
- NumPy
- Pytest
- Docker

## Project Structure
```text
RabTech_Task-6_ML_API/
├── app/
│   └── main.py
├── model/
│   ├── sentiment_model.keras
│   ├── word_index.json
│   └── config.json
├── Tests/
│   └── test_main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
python -m uvicorn app.main:app --reload
```

API URL: `http://127.0.0.1:8000`

Swagger documentation: `http://127.0.0.1:8000/docs`

## API Endpoint

**POST /predict**

Input:
```json
{
  "text": "This movie was amazing!"
}
```

The API returns:
- Review text
- Predicted sentiment
- Probability
- Confidence percentage

## Run Unit Tests

```bash
python -m pytest Tests/test_main.py -v
```

The project successfully passed all four unit tests.

## Docker

Build the Docker image:

```bash
docker build -t sentiment-api .
```

Run the container:

```bash
docker run -p 8000:8000 sentiment-api
```

## Project Outcome

Developed a REST API for real-time sentiment prediction with FastAPI, model integration, unit testing, and Docker configuration.