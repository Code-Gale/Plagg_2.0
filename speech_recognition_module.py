import speech_recognition as sr
recognizer = sr.Recognizer()

def get_user_input():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=3)
            user_input = recognizer.recognize_google(audio)
            print("You:", user_input)
            return user_input
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand you."
        except sr.RequestError:
            return "There was an issue with the speech recognition service."

