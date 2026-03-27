import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json
from apify_client import ApifyClient
import pandas as pd
import time
from google import genai
from google.genai import types
from gemini_analyzer import inferDoc
from r_visualizer import generatePlot
from PIL import Image
from dotenv import load_dotenv
import os





load_dotenv()

client = ApifyClient(os.getenv("APIFY_API_KEY"))

gclient = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))




def loadVideo(filepath: str):
    with open(filepath, "r") as f: 
        return json.load(f)


lottie_url = loadVideo("lottiefiles/Targeting the Ads.json")



with st.container():
    st.set_page_config(page_title= "See The WORLD", page_icon=":ringed_planet:", layout="wide")

    st.subheader("See The WORLD")
    st.title("The World is made by people and people are made of THOUGHTS")
    st.write("See The WORLD project let's you see the Thoughts of the people worldwide on aparticular topic that you decide. These Thoughts are presented to you in an interactive manner. Thus enabling you to SEE what the WORLD thinks about what you are thinking :wave:")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Tech Stack")
        st.write("##")
        st.write("""Streamlit built the web frontend, 
                 backend with python which sends api calls to api that 
                 return a JSON object containing most recent 500 tweets 
                 of people on this particular topic.
                 This response is then sent to google gemini api 
                 which processes the data and returns the specific most used 
                 keywords overall in all the tweets and 3 most used keywords
                 per tweet, with a metadata that contains wheather the 
                 expression is positive or negative. This data is 
                 then fed to models built using R that return with special insights
                 like graphs and most hated and liked keyword.""")
        with right_column:
            st_lottie(lottie_url, height=300, key="coding")

with st.container():
    st.write("---")
    frm = st.form("user query")
    qr = frm.text_input("Enter a word to see world's thought of it.....", key="query")
    btn = frm.form_submit_button("Go!")
    if btn:
        with st.spinner("The World's so big and it takes time to see it all :sweat_smile:"):
            run_input = {
            "searchTerms": [qr],
            "maxItems": 50,
            "sort": "Top", # This gets the "Top" tweets based on engagement
            "tweetLanguage": "en",
            }
            run = client.actor("apidojo/twitter-scraper-lite").call(run_input=run_input)
            tweets = client.dataset(run["defaultDatasetId"]).iterate_items()
            
            if tweets: 
                df = pd.DataFrame(tweets)
                df.to_csv("tweets.csv", index = False)
                for tweet in tweets:
                    with st.chat_message("user", avatar=""):
                        st.write(f"**@{tweet['user']}")
                        st.write(tweet['full text'])
                        st.caption(f"{tweet['favourite_count']} | {tweet['retweet_count']}")
                with st.spinner("Analyzing the thoughts of the world :thinking_face:"):
                    inferDoc(gclient, "tweets.csv", "analyzed_tweets.csv")
                    analyzed_df = pd.read_csv("analyzed_tweets.csv")
                st.success("Analysis Complete!")
                with st.spinner("Generating Graphs and insights :bar_chart:"):
                    generatePlot()
                
                img = Image.open("sentiment_analysis_plot.png")
                st.image(img, captions = "Sentiment Analysis of Tweets")
                
                
                         
                        
            else:
                st.error("No tweets found. Try a different keyword!")
            
                
            