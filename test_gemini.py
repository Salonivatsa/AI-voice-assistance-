from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("API Key not found!")
else:
    print("API Key loaded successfully!")

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents="Say hello"
        )

        print(response.text)

    except Exception as e:
        print("Error:", repr(e))