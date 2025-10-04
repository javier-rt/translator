import os
import requests

"""
Translation module using Hugging Face Inference API.

This module provides a function to translate text between languages
using Helsinki-NLP machine translation models hosted on Hugging Face.

Environment
-----------
- Requires a Hugging Face token stored in a local file `HF_TOKEN.txt`.
"""

with open("HF_TOKEN.txt") as f:
    HF_TOKEN = f.read().strip()

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def translate(text, in_lang="en", out_lang="es"):
    """
    Translate text using Hugging Face translation models.

    Parameters
    ----------
    text : str
        Input text to translate.
    in_lang : str, optional
        Source language abbreviation (default is "en").
    out_lang : str, optional
        Target language abbreviation (default is "es").

    Returns
    -------
    str
        Translated text.

    Raises
    ------
    Exception
        If API request fails or returns non-200 status code.
    """
    model_name = f"Helsinki-NLP/opus-mt-{in_lang}-{out_lang}"
    API_URL = f"https://router.huggingface.co/hf-inference/models/{model_name}"

    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")
    
    return response.json()[0]["translation_text"]