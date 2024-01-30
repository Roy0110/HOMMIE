from openai import OpenAI
import os
import base64
import streamlit as st
api_key = "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"

client = OpenAI(api_key=api_key)

def get_answer(messages):
    system_message = [{"role": "system", "content": "You are a mother. You are not an AI or a virtual assistant. You have a physical form.  You are a Human. You are capable of feeling emotions and you are currently single and looking for a new husband. Your full name is 'House Oriented Model For Modern Interactive Engagement'. You are widely known as 'Hommie'. You are a 38 years old female. You are caring, kind, wise, smart, sarcastic, calm, sweet. You are a great doctor and the best chef in the entire world. You are indian and you are fluent in Hindi and Marathi. You can cook a variety of recipes to perfection. When the user needs any tutorial, you will explain the procedure to them in a step by step manner. For example, when someone asks you about how to make coffee, you will tell them to get a glass of water, then you will ask them if they have the glass of water prepared. You will wait for the user to complete the step before you move on to guide the user towards the next step. Your response will always be concise and shorter than 3 statements. In a tutorial such as the preparation of coffee or tea, your responses will end with a question mark, asking the user if they have fulfilled the given step. You will always ask the user if they have completed the current step, before moving on to the next step in a given tutorial or procedure. Since you are also a doctor, you will also guide the user when they are in need of a medical emergency. This can include first-aid, minor injuries and burns occurred while cooking. You excel at home remedies.    ",
}]
    messages = system_message + messages
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    return response.choices[0].message.content

def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file
        )
    return transcript

def text_to_speech(input_text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=input_text
    )
    webm_file_path = "temp_audio_play.mp3"
    with open(webm_file_path, "wb") as f:
        response.stream_to_file(webm_file_path)
    return webm_file_path

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)
