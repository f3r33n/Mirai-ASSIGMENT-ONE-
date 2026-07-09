import streamlit as st
st.title("ist created chatbot")
personality=st.selectbox("who do u wantto talk to",["a Muslim imam","friendly","sarcastic","professional"], index=None , placeholder="select your personality")
from google import genai
import os 
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key =os.getenv("google_api_key"))
user_message = st.text_input("enter youre message", value=None, placeholder = "here goes  youre message")
if st.button("send"):
    if user_message is None or personality is None:
        st.warning("please enter your message and select your personality")
    else:
        prompt = f"you are a {personality} chatbot. respond to the following message: {user_message}"
        loading_screen = st.empty()
        loading_screen.info("generating response hang on there for a moment...")
        
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        st.success(f"ANSWER: {response.text}")