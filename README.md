# SpeakEasy-Translator

A lightweight **Language Translator App** built using Python, Streamlit, and several supporting libraries. This application translates text into multiple languages using a wrapper around the Google Translate API and provides an audio output via Google's Text-to-Speech (gTTS) engine.

---

## Features

- **Text Translation:** Translate your input text into your selected language.
- **Speech Output:** Listen to the translated text with a generated audio file.
- **Downloadable Audio:** Easily download the audio file of the translation.
- **User-Friendly Interface:** Clean and modern UI built with Streamlit and custom HTML/CSS styling.
- **Language Support:** Uses a CSV dataset for language names and ISO codes for accurate translations.

---

## Technologies Used

- **Python**
- **Streamlit:** For building the frontend.
- **mtranslate:** A lightweight wrapper for the Google Translate API.
- **Pandas:** For handling and processing the language dataset.
- **gTTS:** To convert translated text into speech.
- **Base64:** To encode audio files for download.
- **OS:** For file handling.

---

