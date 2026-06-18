import streamlit as st
from deep_translator import GoogleTranslator


st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2E86C1;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #4CAF50, #2E86C1);
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

.result-box {
    background-color: #E8F6F3;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #2E86C1;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🌍 AI Language Translation Tool</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Translate Text Instantly Between Multiple Languages</p>', unsafe_allow_html=True)

st.divider()

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Italian": "it",
    "Korean": "ko",
    "Portuguese": "pt"
}

# Input Text
text = st.text_area(
    "✍️ Enter Text",
    height=150,
    placeholder="Type your text here..."
)

st.caption(f"Character Count: {len(text)}")

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "📥 Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "📤 Target Language",
        list(languages.keys()),
        index=1
    )

# Translate Button
if st.button("🔄 Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("✅ Translation Completed Successfully!")

            st.markdown("### 📄 Translated Text")

            st.markdown(
                f'<div class="result-box">{translated}</div>',
                unsafe_allow_html=True
            )

            st.text_area(
                "📋 Copy Text",
                value=translated,
                height=120
            )

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()

st.markdown(
    "<center>🚀 Developed for CodeAlpha AI Internship</center>",
    unsafe_allow_html=True
)
