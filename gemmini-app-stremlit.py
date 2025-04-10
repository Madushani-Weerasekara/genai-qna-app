import streamlit as st # To create web app
from dotenv import load_dotenv # To load the environment variable
from langchain_core.prompts import ChatPromptTemplate # 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv() # Loads the variables from .env file


