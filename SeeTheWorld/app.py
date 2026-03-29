import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json
from apify_client import ApifyClient
import pandas as pd
import time
from r_visualizer import generatePlot
from PIL import Image
from dotenv import load_dotenv
import os
import praw
from dotenv import load_dotenv





load_dotenv()








def loadVideo(filepath: str):
    with open(filepath, "r") as f: 
        return json.load(f)


lottie_url = loadVideo("lottiefiles/Targeting_the_Ads.json")

def fetch_reddit_posts(query):
    url = f"https://www.reddit.com/search.json?q={query}&limit=15&sort=top&t=week"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code)
        return []

    try:
        data = response.json()
    except Exception:
        print("Response is not JSON:", response.text[:200])
        return []

    posts = []

    for item in data.get("data", {}).get("children", []):
        post = item.get("data", {})

        posts.append({
            "user": post.get("author"),
            "full_text": (post.get("title", "") + " " + post.get("selftext", "")),
            "favourite_count": post.get("score"),
            "retweet_count": post.get("num_comments")
        })
    return posts


with st.container():
    st.set_page_config(page_title= "See The WORLD", page_icon="🌏", layout="wide")

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
        with st.spinner("The World's so big and it takes time to see it all 😅"):

            tweets = fetch_reddit_posts(qr)

            if len(tweets) > 0:
                try:
                    df = pd.DataFrame(tweets)
                    df.to_csv("tweets.csv", index=False)
                    for tweet in tweets:
                        with st.chat_message("user"):
                            st.write(f"**u/{tweet['user']}**")
                            st.write(tweet['full_text'])
                            st.caption(f"⬆️ {tweet['favourite_count']} 💬 {tweet['retweet_count']}")

                    with st.spinner("Analyzing the thoughts of the world 🤔"):
                        inferDoc("tweets.csv", "analyzed_tweets.csv")

                    st.success("Analysis Complete!")

                    with st.spinner("Generating Graphs 📊"):
                        generatePlot()

                    img = Image.open("sentiment_distribution.png")
                    st.image(img, caption="Sentiment Analysis of Posts")

                except Exception as e:
                    st.error(f"Error: {e}")
                    st.write(tweets[0])

            else:
                st.error("No posts found. Try a different keyword!")
