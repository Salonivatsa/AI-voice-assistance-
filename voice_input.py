import speech_recognition as sr

def listen_voice():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening... Speak now!")

            recognizer.adjust_for_ambient_noise(source, duration=2)


            audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=10
            )

            print("Start speaking...")
            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        print("Processing your voice...")

        text = recognizer.recognize_google(audio, language="en-IN")
        # text = recognizer.recognize_amazon(audio, language="hi-IN")

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