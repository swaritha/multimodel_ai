import whisper

print("Loading Whisper model...")

# tiny (fastest), base (better accuracy), small, medium
model = whisper.load_model("base")

print("Whisper loaded successfully.")


def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe speech from an audio file.
    """

    result = model.transcribe(audio_path)

    return result["text"]