import random
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
#import nltk
#nltk.download('vader_lexicon')

# List of possible therapist responses
therapist_responses = ["Tell me more about it.", "How does that make you feel?", "Why do you think you feel that way?", "What do you think would help in this situation?", "Have you discussed this with anyone else?", "It sounds challenging. Can you elaborate?"]

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    compound_score = sentiment_score['compound']
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"

# Function to generate a therapist response based on sentiment
def generate_response(user_input):
    sentiment = analyze_sentiment(user_input)
    if sentiment == "positive":
        return "That's great to hear! Tell me more."
    elif sentiment == "negative":
        return "I'm sorry to hear that. Can you elaborate?"
    else:
        return random.choice(therapist_responses)

def main():
    st.title("AI Therapist Chatbot")
    st.write("AI Therapist: Hi, I'm here to help. How are you feeling today?")
    user_input = st.text_input("User:")
    if user_input:
        if user_input.lower() == "hey":
            st.text_area("AI Therapist:", value="Hello. How are you doing today?", height=200, max_chars=1000)
        elif user_input.lower() == "bye":
            st.text_area("AI Therapist:", value="Goodbye.", height=200, max_chars=1000)
        else:
            response = generate_response(user_input)
            st.text_area("AI Therapist:", value=response, height=200, max_chars=1000)
            

if __name__ == '__main__':
    main()