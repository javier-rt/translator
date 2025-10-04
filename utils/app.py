import streamlit as st
import time

import utils as utils
import model

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

# Initialize session state at the start
initialize()


def update_steps(num = 1):
    st.session_state.step = num


with st.container(border=True):
    col1, col2 = st.columns([1, 1])

    with col1:
        lang_source = st.selectbox(
            "Choose source language",
            options=lang.values(),
            index=7,
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
            index=30,
            key="lang_target",
        )

        step = st.session_state.step
        
        if step == 1:
            st.write("Waiting text...")
        elif step == 2:
            st.write("Translating text...")
            with st.container(border=False):
                st.write("")

            start_time = time.perf_counter()
            
            try:
                original_text = st.session_state.original_text
                ab_source = utils.ab_language(st.session_state.lang_source)
                ab_target = utils.ab_language(st.session_state.lang_target)

                st.session_state.translation = model.translate(original_text, ab_source, ab_target)

            except Exception as e:
                st.error(f"{str(e)} - Restasting app...")

                time.sleep(3)
                update_steps()
                st.rerun()

            end_time = time.perf_counter()
            st.session_state.time = round(end_time - start_time, 2)

            update_steps(3)
            st.rerun()

        else:
            st.write(f"Translated text - Time spent translating: {st.session_state.time}s")
            with st.container(border=False):
                st.write(st.session_state.translation)
                translation = st.session_state.translation

                # if st.button("Copy to clipboard"):
                    # st.markdown(f"""
                    #     <textarea id="copy_text" style="display:none">{translation}</textarea>
                    #     <button onclick="navigator.clipboard.writeText(document.getElementById('copy_text').value)">
                    #         Copy to clipboard
                    #     </button>
                    #     """, unsafe_allow_html=True)



if st.button("Translate"):
    update_steps(2)
    
    st.rerun()
