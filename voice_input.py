# import speech_recognition as sr

# def listen_voice():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")

#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     try:
#         text = recognizer.recognize_google(audio)
#         print(f"You said: {text}")
#         return text
    
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand the audio.")
#         return None
    
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")
#         return None

import speech_recognition as sr

def listen_voice():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening... Speak now!")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Start speaking...")
            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        print("Processing your voice...")

        text = recognizer.recognize_google(audio, language="en-IN")

        print("You said:", text)
        return text

    except sr.WaitTimeoutError:
        print("No voice detected. Please try again.")
        return ""

    except sr.UnknownValueError:
        print("Could not understand your voice.")
        return ""

    except sr.RequestError as e:
        print("Internet or recognition service error:", e)
        return ""

    except Exception as e:
        print("Error:", e)
        return ""