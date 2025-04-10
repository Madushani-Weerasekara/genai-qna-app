import streamlit as st # To create web app
from dotenv import load_dotenv # To load the environment variable
from langchain_core.prompts import ChatPromptTemplate # 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv() # Loads the variables from .env file


# Now we can instantiate our model object and generate chat completions
llm = ChatGoogleGenerativeAI(
    model = "gemmini - 1.5-pro",
    temperatuere = 0,
    max_tokens= None,
    timeout=None,
    max_retries=2
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a chatbot"),
        ("Human", "Question : {question}")

    ]
)

st.title('Langchain Demo with Gemini')
input_text = st.time_input("Enter your question here")