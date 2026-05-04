from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import streamlit as st

model_name = "facebook/mbart-large-50-many-to-many-mmt"

# ✅ Cache model (loads only once)
@st.cache_resource
def load_model():
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model


LANG_MAP = {
    "English → Hindi": ("en_XX", "hi_IN"),
    "English → French": ("en_XX", "fr_XX"),
    "English → Japanese": ("en_XX", "ja_XX")
}


def translate(text, option):
    tokenizer, model = load_model()  # ✅ use cached model

    src_lang, tgt_lang = LANG_MAP[option]

    tokenizer.src_lang = src_lang
    encoded = tokenizer(text, return_tensors="pt")

    generated = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang]
    )

    return tokenizer.decode(generated[0], skip_special_tokens=True)