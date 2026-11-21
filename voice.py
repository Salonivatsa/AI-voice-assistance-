import streamlit as st
import speech_recognition as sr
import edge_tts
import sounddevice as sd

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

print(" libraries imported successfully!")



