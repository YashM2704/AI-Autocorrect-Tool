import streamlit as st
from hybrid_autocorrect import hybrid_autocorrect

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="AI Autocorrect Tool",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== CUSTOM CSS =====================
st.markdown("""
    <style>
    .main {
        background-color: #0F1117;
    }
    
    .title {
        font-size: 48px;
        font-weight: 700;
        background: linear-gradient(90deg, #00ff88, #00ccff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 8px;
    }
    
    .subtitle {
        font-size: 20px;
        color: #b0b0b0;
        text-align: center;
        margin-bottom: 40px;
    }
    
    .stTextArea textarea {
        background-color: #1E2128 !important;
        color: white !important;
        font-size: 17px !important;
        border-radius: 12px !important;
        border: 2px solid #333 !important;
    }
    
    .result-card {
        background-color: #1E2128;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #333;
        margin-bottom: 20px;
    }
    
    .original {
        border-left: 5px solid #ff5555;
    }
    
    .corrected {
        border-left: 5px solid #00ff88;
    }
    
    .btn-run {
        background: linear-gradient(90deg, #00ff88, #00ccff);
        color: black;
        font-weight: bold;
        border-radius: 50px;
        padding: 12px 40px;
        font-size: 18px;
        transition: all 0.3s;
    }
    
    .btn-run:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 255, 136, 0.3);
    }
    
    .highlight {
        background-color: #2A2F3A;
        padding: 2px 8px;
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

# ===================== SIDEBAR =====================
with st.sidebar:
    st.title("⚙️ Settings")
    st.divider()
    
    show_predictions = st.checkbox("Show BERT Predictions", value=True)
    show_preprocessing = st.checkbox("Show NLP Processing Steps", value=False)
    
    st.divider()
    st.caption("Built with ❤️ using Streamlit + BERT + TextBlob")

# ===================== MAIN CONTENT =====================
st.markdown('<p class="title">🚀 AI Autocorrect Tool</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Context-Aware Spelling & Grammar Correction using TextBlob + BERT</p>', 
            unsafe_allow_html=True)

# Input Section
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.subheader("✍️ Enter Your Sentence")
    user_input = st.text_area(
        label="",
        height=160,
        placeholder="Type here... (e.g., I havv a dreem or Thsi is an amzing tool)",
        label_visibility="collapsed"
    )

    # Run Button
    if st.button("🚀 Run AI Autocorrect", use_container_width=True, type="primary"):
        if user_input.strip() == "":
            st.error("Please enter some text to correct.")
        else:
            with st.spinner("Applying AI magic..."):
                result = hybrid_autocorrect(user_input)

            st.success("✅ Correction Complete!")

            # ===================== RESULTS =====================
            st.divider()
            
            c1, c2 = st.columns(2)
            
            with c1:
                st.markdown("### 📌 Original Text")
                st.markdown(f"""
                <div class="result-card original">
                    {result['original_text']}
                </div>
                """, unsafe_allow_html=True)
            
            with c2:
                st.markdown("### ✅ Corrected Text")
                st.markdown(f"""
                <div class="result-card corrected">
                    <strong>{result['textblob_output']}</strong>
                </div>
                """, unsafe_allow_html=True)

            # NLP Pipeline
            if show_preprocessing:
                st.divider()
                st.subheader("🧹 NLP Processing Pipeline")
                cols = st.columns(5)
                steps = ["Lowercasing", "Tokenization", "Stopword Removal", "Lemmatization", "Spell Correction"]
                for i, step in enumerate(steps):
                    with cols[i]:
                        st.success(step)

            # BERT Predictions
            if show_predictions and result.get("bert_suggestions"):
                st.divider()
                st.subheader("🧠 BERT Contextual Suggestions")
                
                for i, suggestion in enumerate(result["bert_suggestions"]):
                    st.markdown(f"**Masked Sentence {i+1}:**")
                    st.code(suggestion["masked_sentence"], language="text")
                    
                    st.markdown("**Top Predictions:**")
                    for pred in suggestion["predictions"]:
                        st.info(f"✔ {pred}")
                    st.markdown("---")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>Made with Python, Streamlit, TextBlob & BERT</p>",
    unsafe_allow_html=True
)