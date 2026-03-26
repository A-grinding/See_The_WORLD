import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json


def loadVideo(url):
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

lottie_url = loadVideo("https://app.lottiefiles.com/share/6d831349-4577-498f-aab9-ca1913426abe")


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
