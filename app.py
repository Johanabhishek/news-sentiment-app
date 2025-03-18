import streamlit as st
from news_sentiment import extract_news, analyze_sentiment, generate_hindi_speech
import os

# Streamlit UI
st.title("📢 Company News Sentiment Analysis with Hindi Speech")
st.write("Enter a company name to analyze its latest news sentiment.")

# User Input
company = st.text_input("Enter Company Name", "")

if st.button("Analyze News"):
    if company:
        news_list = extract_news(company)
        
        if not news_list:
            st.error("No news found. Try another company.")
        else:
            st.subheader(f"🔎 News Results for: {company}")
            
            summary_text = ""
            for i, news in enumerate(news_list):
                sentiment = analyze_sentiment(news["title"])
                st.write(f"**{i+1}. {news['title']}**")
                st.write(f"📌 Sentiment: **{sentiment}**")
                st.write(f"[🔗 Read More]({news['link']})")
                st.write("---")
                summary_text += news["title"] + ". "  # Combine summaries for TTS
            
            # Convert to Hindi Speech
            speech_file = generate_hindi_speech(summary_text)
            st.subheader("🔊 Listen to Summary in Hindi")
            st.audio(speech_file)
    else:
        st.error("Please enter a company name.")
