from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

print("Loading FLAN-T5...")

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("FLAN-T5 Loaded")


def generate_answer(prompt: str):

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=150
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )