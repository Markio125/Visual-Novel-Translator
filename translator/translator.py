from transformers import MarianTokenizer, MarianMTModel, pipeline
from fastapi import FastAPI
import uvicorn

tokenizer = MarianTokenizer.from_pretrained(f"translation_model/tokenizer")
model = MarianMTModel.from_pretrained(f"translation_model/model")
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device="cpu")

def translate_text(text):
    result = pipe(text, max_length=256)
    return result[0]['generated_text']

app = FastAPI()

@app.get("/")
def read_root():
    return {"App Status": "Running"}

@app.get("/translate")
def translate(text : str):
    sentence = translate_text(text)
    return {"translated_text": sentence}

if __name__ == "__main__":
    uvicorn.run("translator:app", host="127.0.0.1", port=8000, reload=True)