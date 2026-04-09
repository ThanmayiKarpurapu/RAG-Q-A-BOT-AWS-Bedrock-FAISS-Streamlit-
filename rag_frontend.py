# rag_frontend.py

# rag_frontend.py

import streamlit as st
import rag_backend as demo

st.set_page_config(page_title="HR Q&A with RAG", layout="wide")

# -------- STYLE --------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    h1, h2, h3, p, div {
        color: white !important;
    }

    .stTextArea textarea {
        background-color: #1e1e1e;
        color: white;
        border-radius: 10px;
    }

    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center;'>💼 HR Q & A with RAG 🤖</h1>",
    unsafe_allow_html=True
)

input_text = st.text_area("Ask your HR question:")

if st.button("🚀 Get Answer"):
    if input_text.strip() == "":
        st.warning("Enter a question")
    else:
        with st.spinner("Thinking..."):
            response = demo.hr_rag_response(input_text)
            st.success("Answer:")
            st.write(response)