# Translator 🌍

A simple but powerful translation app built with **Streamlit** and the **Hugging Face Inference API**.
It uses [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) machine translation models (`opus-mt`) to translate text between many different languages.

---

## 🚀 Features

* Translate text between 30+ languages.
* Lightweight & fast: Uses Hugging Face Inference API, no local model downloads needed.
* Fast and easy-to-use Streamlit web app.
* Automatically measures translation time.
* Clean interface with source/target language selectors.

---

## 📂 Project Structure

```
translator/
│── LICENSE
│── main.py             # Entry point, launches Streamlit app
│── README.md           # Project documentation
│── requirements.txt    # Python dependencies
│── HF_TOKEN.txt        # Your Hugging Face API token (ignored in git)
│── utils/
    │── app.py          # Streamlit UI
    │── languages.py    # Supported languages and abbreviations
    │── model.py        # Translation logic using Hugging Face API
    │── utils.py        # Helper functions
```

---

## ⚙️ Requirements

* Python 3.9+ recommended
* [Streamlit](https://streamlit.io/)
* [Requests](https://docs.python-requests.org/en/master/)

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Hugging Face Token

This project requires a personal Hugging Face API token.

1. Create an account at [huggingface.co](https://huggingface.co).
2. Get your **Access Token** from your profile settings.
3. Create a file called `HF_TOKEN.txt` inside the project root (`translator/`) and paste your token there.

⚠️ `HF_TOKEN.txt` is already in `.gitignore`, so your token stays private.

---

## ▶️ Run the App

Simply run:

```
python main.py
```

This will launch Streamlit and open the app in your browser.

---

## 🌐 How It Works

1. You type in some text and pick the **source** and **target** languages.
2. The app sends your text to Hugging Face Inference API, so no models are downloaded locally and it stays lightweight, even on computers with low memory.
3. The app automatically builds the correct model name for the language pair, e.g.:

   ```
   Helsinki-NLP/opus-mt-en-es
   ```

   (English → Spanish).
3. It sends the text to Hugging Face’s Inference API and displays the translation.

---

## 🗣️ Supported Languages

Some of the supported languages include:
Arabic, Chinese, Dutch, English, French, German, Greek, Hindi, Italian, Japanese, Korean, Portuguese, Russian, Spanish, Turkish, Vietnamese, and many more.
(See `utils/languages.py` for the full list).

---

## 📜 License

This project is licensed under the terms of the **GNU General Public License v3.0 (GPL-3.0)**.
See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

* [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) for the translation models.
* [Hugging Face](https://huggingface.co/) for hosting and providing the API.
* [Streamlit](https://streamlit.io/) for making interactive apps super easy.