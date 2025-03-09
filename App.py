import streamlit as st  # Library for frontend in python.
from mtranslate import translate # It is the library used for translating text from one language to another.
#It acts as a lightweight wrapper for the Google Translate API and allows you to easily perform translations directly in your Python application.
import pandas as pd
import os # It is the library used to interact with the operating system.
from gtts import gTTS # Here gTTS stands for the google text to speech library using Google Translate's TTS engine. 
#It supports multiple languages and can save the speech as an audio file.
import base64 #The base64 library in Python is used to encode and decode data using Base64, a binary-to-text encoding scheme. Base64 is commonly used to encode binary data (e.g., images, audio) into a text format that can be easily transmitted over text-based protocols like HTTP, HTML, or JSON.

# Load language dataset
df = pd.read_csv(r"F:\Data Science Projects\Language Translator\language.csv")
df.dropna(inplace=True) # will remove any row containing any nan values in it.
lang = df['name'].to_list() #Selects the name column from the Dataset. 
langlist = tuple(lang) #converting the selected name column into the tuple.
langcode = df['iso'].to_list() # It is to select the iso codes of the language.

# Create dictionary of language and 2-letter langcode
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# App Layout
st.set_page_config(page_title="Language Translation App", layout="wide", page_icon="🌍")

# Header with a catchy title
st.markdown(
    """
    <style>
        .main-title {
            font-size: 3rem;
            text-align: center;
            color: #2b5876;
            font-family: Arial, sans-serif;
        }
        .subtitle {
            font-size: 1.2rem;
            text-align: center;
            color: #333333;
            margin-bottom: 2rem;
        }
    </style>
    <div>
        <h1 class="main-title">🌍 Language Translator</h1>
        <p class="subtitle">Translate text into multiple languages with speech output!</p>
    </div>
    <style>
        .stApp {
            background: linear-gradient(to bottom right,rgb(85, 187, 190),rgb(130, 225, 231));
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Input Section
with st.container():
    st.markdown("#### Enter Text to Translate")
    inputtext = st.text_area("Type your text here...", height=150)

# Sidebar
st.sidebar.header("Select Language")
choice = st.sidebar.radio("Choose a language:", langlist)
st.sidebar.markdown("### 🌟 Features")
st.sidebar.markdown("- Supports text translation")
st.sidebar.markdown("- Audio file for supported languages")
st.sidebar.markdown("- Easy download option")

speech_langs = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "gu": "Gujarati",
    "od": "odia",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "la": "Latin",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-CN": "Chinese",
}

# Function to decode audio file for download
def get_binary_file_downloader_html(bin_file, file_label="File"):  # The bin_file is the file path that need to be dowmload, file_label is basically the file name.
    with open(bin_file, "rb") as f: #To open that file in binary mode.
        data = f.read() #Reading the file.
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

# Display output and additional features
if len(inputtext) > 0:
    try:
        # Translation
        output = translate(inputtext, lang_array[choice])
        with st.container():
            st.markdown("#### Translated Text")
            st.text_area("", output, height=150)
        
        # Speech Output
        if choice in speech_langs.values():
            aud_file = gTTS(text=output, lang=lang_array[choice], slow=False)
            aud_file.save("lang.mp3")
            with st.container():
                st.markdown("#### 🎧 Listen to the Translation")
                audio_file_read = open("lang.mp3", "rb")
                audio_bytes = audio_file_read.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.markdown(get_binary_file_downloader_html("lang.mp3", "Audio File"), unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer the bottom most part of the frontend
st.markdown(
    """
    <style>
        .footer {
            font-size: 0.9rem;
            text-align: center;
            color: #888888;
            margin-top: 3rem;
        }
    </style>
    <div class="footer">
        Created with ❤️ by Karishma Jaiswal
    </div>
    """,
    unsafe_allow_html=True,
)
