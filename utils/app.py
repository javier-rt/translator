import streamlit as st
import time
import model
import utils as utils

from languages import LANGUAGES as lang

st.title("Translator")

st.set_page_config(
    page_title="Translator",
    layout="wide",
)

def initialize():
    if "step" not in st.session_state:
        st.session_state.step = 1
    if "translate_area" not in st.session_state:
        st.session_state.translate_area = " "

initialize()

def update_steps(num = 1):
    st.session_state.step = num

with st.container(border=True):
    col1, col2 = st.columns([1, 1])

    with col1:
        lang_source = st.selectbox(
            "Choose source language",
            options=lang.values(),
            index=0,
            key="lang_source",
        )
        original_text = st.text_area(
            "Original text",
            value="",
            placeholder="Type to translate",
            key="original_text",
        )

    with col2:
        lang_target = st.selectbox(
            "Choose target language",
            options=lang.values(),
            index=31,
            key="lang_target",
        )

        step = st.session_state.step
        
        if step == 1:
            st.write("Waiting text...")
        elif step == 2:
            st.write("Translating text...")
            with st.container(border=False):
                st.write("")

            original_text = st.session_state.original_text
            ab_source = utils.ab_language(st.session_state.lang_source)
            ab_target = utils.ab_language(st.session_state.lang_target)
            st.session_state.lang_detected = ""

            if ab_source == "auto":
                ab_source, lang_score = model.auto_detect_language(original_text)
                lang_source = lang.get(ab_source, "Unknown")
                st.session_state.lang_detected = f"- Language detected: {lang_source}"
            
            try:
                start_time = time.perf_counter()
                st.session_state.translation = model.translate(original_text, ab_source, ab_target)
                end_time = time.perf_counter()

            except Exception as e:
                st.error(f"{str(e)} - Restasting app...")

                time.sleep(3)
                update_steps()
                st.rerun()

            st.session_state.time = round(end_time - start_time, 2)

            update_steps(3)
            st.rerun()

        else:
            st.write(f"Translated text - Time spent translating: {st.session_state.time}s {st.session_state.lang_detected}")
            with st.container(border=False):
                st.write(st.session_state.translation)

if st.button("Translate"):
    update_steps(2)
    st.rerun()
