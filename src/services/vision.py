from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

print("Loading BLIP model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("BLIP loaded successfully.")


def generate_caption(image_path: str) -> str:
    """
    Generate an image caption using BLIP.
    """

    image = Image.open(image_path).convert("RGB")

    inputs = processor(image, return_tensors="pt")

    output = model.generate(**inputs)

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption