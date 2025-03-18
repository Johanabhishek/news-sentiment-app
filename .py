import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os

# Download required NLTK data
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def extract_news(company):
    """Scrapes Google News for articles related to a company."""
    url = f"https://news.google.com/search?q={company}&hl=en&gl=US&ceid=US:en"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.find_all("h3")[:10]:  # Get top 10 articles
        title = item.text
        link = "https://news.google.com" + item.a["href"][1:]  # Fix relative URL
        articles.append({"title": title, "link": link})
    
    return articles

def analyze_sentiment(text):
    """Performs sentiment analysis and returns Positive, Negative, or Neutral."""
    score = sia.polarity_scores(text)["compound"]
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

def generate_hindi_speech(text, filename="output.mp3"):
    """Converts text to Hindi speech."""
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename
