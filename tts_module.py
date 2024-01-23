import pyttsx3

def speak(text):
    print("Response:", text)
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)  # Adjust the rate for faster speech
    engine.say(text)
    engine.runAndWait()
