import streamlit as st
from translator import translate, LANG_MAP   # ✅ changed here

st.set_page_config(page_title="Translator")

st.title("🌍 Language Translation Model")

try:
    option = st.selectbox("Choose Language", list(LANG_MAP.keys()))  # ✅ changed here

    text = st.text_area("Enter text")

    if st.button("Translate"):
        if text.strip():
            with st.spinner("Translating... please wait ⏳"):
                 result = translate(text, option)

            st.success(result)
        else:
            st.warning("Enter some text")

except Exception as e:
    st.error(f"Error: {e}")