# Multimodal AI Backend API

A FastAPI-based backend application that processes **text**, **images**, and **audio** using AI models and generates an intelligent response through multimodal fusion.

---

## Features

- Image Captioning using BLIP
- Speech-to-Text using Whisper
- Multimodal Prompt Fusion
- Text Generation using FLAN-T5
- REST API built with FastAPI
- Interactive API Documentation (Swagger)
- Docker Support
- Unit Testing with Pytest

---

## Tech Stack

- Python 3.13
- FastAPI
- Transformers
- BLIP Image Captioning Model
- OpenAI Whisper
- Google FLAN-T5
- PyTorch
- Docker
- Pytest

---

## Project Structure

```
multimodel_ai/
│
├── src/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── exceptions.py
│   │
│   └── services/
│       ├── vision.py
│       ├── audio.py
│       ├── fusion.py
│       └── llm.py
│
├── tests/
│   └── test_api.py
│
├── uploads/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .env.example
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/swaritha/multimodel_ai

cd multimodel_ai
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn src.main:app --reload
```

The server will start at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy"
}
```

---

### Image Analysis

```
POST /api/v1/analyze/image
```

Input

- JPG
- PNG

Response

```json
{
  "caption": "A dog running on the grass."
}
```

---

### Audio Analysis

```
POST /api/v1/analyze/audio
```

Input

- MP3
- WAV

Response

```json
{
  "transcript": "Hello everyone."
}
```

---

### Multimodal Processing

```
POST /api/v1/process
```

Accepts

- Text
- Image
- Audio

Response

```json
{
  "response": "The image shows a dog playing in a park.",
  "context_used": [
    "text",
    "image",
    "audio"
  ]
}
```

---

## AI Models Used

| Task | Model |
|------|------|
| Image Captioning | Salesforce BLIP |
| Speech Recognition | OpenAI Whisper |
| Text Generation | Google FLAN-T5 |

---

## Running Tests

```bash
pytest
```

Example Output

```
2 passed
```

---

## Docker

Build

```bash
docker build -t multimodel-api .
```

Run

```bash
docker run -p 8000:8000 multimodal-api
```

---

