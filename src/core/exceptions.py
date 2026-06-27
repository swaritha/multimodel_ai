from fastapi import HTTPException


def invalid_image():
    raise HTTPException(
        status_code=400,
        detail="Only JPG and PNG images are allowed."
    )


def invalid_audio():
    raise HTTPException(
        status_code=400,
        detail="Only MP3 and WAV audio are allowed."
    )