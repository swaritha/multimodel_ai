def build_prompt(
    text_input=None,
    image_caption=None,
    audio_transcript=None,
):
    prompt = """You are a helpful AI assistant.

Answer the user's question using all the available context.

"""

    if image_caption:
        prompt += f"\nImage Description:\n{image_caption}\n"

    if audio_transcript:
        prompt += f"\nAudio Transcript:\n{audio_transcript}\n"

    if text_input:
        prompt += f"\nUser Text:\n{text_input}\n"

    prompt += "\nAnswer:\n"

    return prompt