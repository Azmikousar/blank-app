import streamlit as st

st.set_page_config(page_title="AI Studio")

menu = st.sidebar.selectbox(
    "Choose Tool",
    [
        "Home",
        "Chatbot",
        "Image Generator",
        "Document QA",
        "Content Generator"
    ]
)

if menu == "Home":
    st.title("🏠 Home")

elif menu == "Chatbot":
    st.title("🤖 Chatbot")

elif menu == "Image Generator":
    st.title("🎨 Image Generator")

elif menu == "Document QA":
    st.title("📄 Document QA")

elif menu == "Content Generator":
    st.title("✍️ Content Generator")
