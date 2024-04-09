import streamlit as st

import ytVideoSummarizer as yt, invoiceExtractor as invoice, qaChatBot as chatbot

# Page functions
def youtube_video_summarizer():
    yt.main()

def invoice_extractor():
    invoice.main()

def chat_bot():
    chatbot.main()

# Sidebar title
st.sidebar.markdown(
"""
<style>
.sidebar-title {
    font-size: 24px;
    font-weight: bold;
    color: #ffffff;
    background-color: #000000;
    padding: 10px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<p class="sidebar-title">AI Application</p>', unsafe_allow_html=True)

# Sidebar radio buttons
page_options = {
    "YouTube Video Summary": youtube_video_summarizer,
    "Invoice Extractor": invoice_extractor,
    "Chat Bot": chat_bot
}
page = st.sidebar.radio("", list(page_options.keys()))

# Run the selected page function
page_options[page]()
