import streamlit as st
from streamlit_mic_recorder import mic_recorder

st.title("Mic Test")

audio = mic_recorder(
    start_prompt="🎙 Start Recording",
    stop_prompt="⏹ Stop Recording",
    key="mic"
)

if audio:
    st.success("Recording captured")

    st.audio(
        audio["bytes"],
        format="audio/wav"
    )

    st.write(audio)