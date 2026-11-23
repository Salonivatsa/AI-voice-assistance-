# # llm brain 
# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY"),
#     temperature=0.7
# )

# def get_ai_response(user_input):

#     response = llm.invoke(user_input)

#     return response.content

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def get_ai_response(user_input):

    try:
        response = llm.invoke(user_input)
        return response.content

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, I am unable to connect right now."