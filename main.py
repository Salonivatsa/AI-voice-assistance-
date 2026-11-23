from voice_input import listen_voice

# user voice
# text = listen_voice()
# print("User Input:" , text)

# voice input connect with ai

from llm import get_ai_response

user_text = listen_voice()

if user_text:
    print("\nThinking...")

    answer = get_ai_response(user_text)

    print("\nTalkWithAI:", answer)