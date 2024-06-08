import streamlit as st
import pandas as pd
import os
import requests
from io import BytesIO
from streamlit_mic_recorder import mic_recorder
import assemblyai as aai
import datetime
from PIL import Image
import io


st.title("Audio Transcription App")

audio = mic_recorder(start_prompt="Start recording", stop_prompt="Stop recording", just_once=False,
                     use_container_width=False, callback=None, args=(), kwargs={}, key=None)

if audio is not None:
    if isinstance(audio, dict) and 'bytes' in audio:
        audio_bytes = audio['bytes']
        st.audio(audio_bytes, format='audio/wav')

        filename = (datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_feedback.wav")
        with open(filename, "wb") as f:
            f.write(audio_bytes)
