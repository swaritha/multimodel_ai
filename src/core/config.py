from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "google/flan-t5-base"
)

UPLOAD_FOLDER = "uploads"

ALLOWED_IMAGE = [
    "image/jpeg",
    "image/png"
]

ALLOWED_AUDIO = [
    "audio/mpeg",
    "audio/wav",
    "audio/x-wav"
]