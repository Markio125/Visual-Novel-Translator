import requests
from ocr import jpn_ocr

base_url = "http://127.0.0.1:8000/translate"


def translate(jp_text):
    params = {"text": jp_text}
    response = requests.get(base_url, params=params)
    return response.json()['translated_text']

# trial run
# jp_text = jpn_ocr('snips/2.png')
# print(jp_text)
#
# params = {"text": jp_text}
#
# response = requests.get(base_url, params=params)
#
# print(response.json()['translated_text'])