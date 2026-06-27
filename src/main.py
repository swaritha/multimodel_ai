from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from src.services.vision import generate_caption
from src.services.audio import transcribe_audio
from fastapi import Form

from src.services.fusion import build_prompt
from src.services.llm import generate_answer

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
app = FastAPI(
    title="Multimodal AI Backend",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Multimodal AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/api/v1/analyze/image")
async def analyze_image(
    image: UploadFile = File(...)
):

    if image.content_type not in [
        "image/jpeg",
        "image/png"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Only JPG and PNG images are allowed."
        )

    file_path = UPLOAD_DIR / image.filename

    with open(file_path, "wb") as f:
        f.write(await image.read())

    caption = generate_caption(str(file_path))

    return JSONResponse(
        {
            "caption": caption
        }
    )


@app.post("/api/v1/analyze/audio")
async def analyze_audio(
    audio: UploadFile = File(...)
):

    if audio.content_type not in [
        "audio/mpeg",
        "audio/wav",
        "audio/x-wav"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Only MP3 and WAV audio are allowed."
        )

    file_path = UPLOAD_DIR / audio.filename

    with open(file_path, "wb") as f:
        f.write(await audio.read())

    transcript = transcribe_audio(str(file_path))

    return JSONResponse(
        {
            "transcript": transcript
        }
    )
@app.post("/api/v1/process")
async def process_request(
    text_input: str = Form(None),
    image: UploadFile = File(None),
    audio: UploadFile = File(None),
):

    if text_input is None and image is None and audio is None:
        raise HTTPException(
            status_code=400,
            detail="At least one input is required."
        )

    image_caption = None
    audio_transcript = None

    context_used = []

    if image:

        image_path = UPLOAD_DIR / image.filename

        with open(image_path, "wb") as f:
            f.write(await image.read())

        image_caption = generate_caption(str(image_path))

        context_used.append("image")

    if audio:

        audio_path = UPLOAD_DIR / audio.filename

        with open(audio_path, "wb") as f:
            f.write(await audio.read())

        audio_transcript = transcribe_audio(str(audio_path))

        context_used.append("audio")

    if text_input:
        context_used.append("text")

    prompt = build_prompt(
        text_input,
        image_caption,
        audio_transcript
    )

    answer = generate_answer(prompt)

    return {
        "response": answer,
        "context_used": context_used
    }
