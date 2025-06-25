# This file should only be run once ideally

import torch
from transformers import MarianTokenizer, MarianMTModel, pipeline

model_name = "Markio/fine-tuned-opus-mt-ja-en"

# tokenizer = MarianTokenizer.from_pretrained(model_name)
# tokenizer.save_pretrained(f"translation_model/tokenizer")
# model = MarianMTModel.from_pretrained(model_name)
# model.save_pretrained(f"translation_model/model")

# Trial Run

tokenizer = MarianTokenizer.from_pretrained(f"translation_model/tokenizer")
model = MarianMTModel.from_pretrained(f"translation_model/model")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=device)
sentence = pipe("これはモデルがうまく動作しているかどうかを確認するためのテスト文です")
print(sentence)