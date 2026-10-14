import streamlit as st
from textblob import TextBlob

st.title("AI Sentiment Analyzer")
text = st.text_input("Enter text to analyze:")
if text:
    score = TextBlob(text).sentiment.polarity
    st.write(f"Result: {'Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral'}")
