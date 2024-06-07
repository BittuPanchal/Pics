import streamlit as st
import pandas as pd
import os
from streamlit_mic_recorder import mic_recorder
import assemblyai as aai
import datetime
from PIL import Image
import io

aai.settings.api_key = "1af9cefd457041d0a0a709c9563bc6d0"

st.title("Audio Transcription App")

clinician_name = st.text_input("Enter Your Name")
patient_name = st.text_input("Enter Patient Name")
patient_mrn = st.text_input("Enter Patient MRN")

if st.checkbox("Take a picture"):
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        bytes_data = img_file_buffer.getvalue()

def transcribe_audio(file_path):
    transcribed_text = ""
    try:
        with open(file_path, 'rb') as f:
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(f)

        if transcript.status == aai.TranscriptStatus.error:
            st.error("Transcription Error: " + transcript.error)
        else:
            transcribed_text = transcript.text
            #st.success("Transcription: " + transcript.text)
            transcribed_text = st.text_area("Edit your transcription:", transcript.text)
            
    except Exception as e:
        st.error("Error occurred during transcription: " + str(e))
    
    return transcribed_text
    
audio = mic_recorder(start_prompt="Start recording", stop_prompt="Stop recording", just_once=False,
                     use_container_width=False, callback=None, args=(), kwargs={}, key=None)

if audio is not None:
    if isinstance(audio, dict) and 'bytes' in audio:
        audio_bytes = audio['bytes']
        st.audio(audio_bytes, format='audio/wav')

        database_path = r'C:\Users\Bittu - HL008\Desktop\Text Voice\OASIS Database'
        os.makedirs(database_path, exist_ok=True)
        
        folder_name = datetime.datetime.now().strftime("%m-%d-%Y")
        folder_path = os.path.join(database_path, folder_name, clinician_name, patient_mrn)
        os.makedirs(folder_path, exist_ok=True)

        filename = os.path.join(folder_path, f"{clinician_name}_{patient_name}_{patient_mrn}_feedback.wav")
        with open(filename, "wb") as f:
            f.write(audio_bytes)

        img_filename = os.path.join(folder_path, f"{clinician_name}_{patient_name}_{patient_mrn}_feedback.jpg")
        with open(img_filename, "wb") as f:
            f.write(bytes_data)
        
        transcribed_text = transcribe_audio(filename)

        if st.button("Save"):
            os.chdir(database_path)
            df1 = pd.read_excel('Database.xlsx')
            data = [[folder_name, clinician_name, patient_name, patient_mrn, filename, transcribed_text]]
            df2 = pd.DataFrame(data, columns=df1.columns.tolist())
            df = pd.concat([df1, df2], ignore_index=True)
            df = df.drop_duplicates(subset=df.columns.tolist(), keep='last')
            df.to_excel('Database.xlsx', index=False)
            st.success(f"Audio saved as {filename} on your desktop and Data is saved in Database.xlsx")
