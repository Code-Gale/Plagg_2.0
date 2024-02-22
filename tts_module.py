import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 200)  # Adjust the rate for faster speech



def speak(text):
    print("Response:", text)
    engine.say(text)
    engine.runAndWait()
