import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os

# Download required NLTK data
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    # Function logic here
    return "Positive"  # Example return value


def extract_news(company):
    url = f"https://news.google.com/search?q={company}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_items = soup.find_all("article")  # Adjust selector if needed
    news_list = []

    for item in news_items:
        if item.a:  # ✅ Check if <a> tag exists before accessing href
            link = "https://news.google.com" + item.a["href"][1:]  # Fix relative URL
            title = item.a.get_text(strip=True)
            news_list.append({"title": title, "link": link})
        else:
            print("Skipping an article without a link")  # Debugging info

    return news_list

def generate_hindi_speech(text, filename="output.mp3"):
    """Converts text to Hindi speech."""
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename
