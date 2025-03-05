import os
import openai
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if not api_key:
    st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
else:
    openai.api_key = api_key

    # Make a test API call to OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello, OpenAI!"}]
        )
        st.success("API call successful!")
        st.write("Test response:", response["choices"][0]["message"]["content"])

    except Exception as e:  # ✅ Added this missing block
        st.error(f"Error in API call: {e}")
