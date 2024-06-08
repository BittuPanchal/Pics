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

clinician_name = st.text_input("Enter Your Name")
patient_mrn = st.text_input("Enter Patient MRN")

audio = mic_recorder(start_prompt="Start recording", stop_prompt="Stop recording", just_once=False,
                     use_container_width=False, callback=None, args=(), kwargs={}, key=None)

if audio is not None:
    if isinstance(audio, dict) and 'bytes' in audio:
        audio_bytes = audio['bytes']
        st.audio(audio_bytes, format='audio/wav')

        filename = f"{clinician_name}_{patient_mrn}_feedback.wav"
        with open(filename, "wb") as f:
            f.write(audio_bytes)
