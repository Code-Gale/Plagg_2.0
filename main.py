from datetime import datetime
import time
from tts_module import speak
from weather_module import get_weather
from news_module import get_news
from time_module import get_current_time
from math_module import solve_math_problem
from wikipedia_module import get_wikipedia_info
from location_module import get_current_location
from dictionary_module import get_word_definition
from jokes_module import get_joke
from trivia_module import get_random_trivia
from unit_conversion_module import convert_units
from speech_recognition_module import get_user_input

def greet_user():
    # Greet user based on the current time
    current_time = datetime.now().time()
    if current_time.hour < 12:
        speak("Good morning!")
        speak("I am Plagg, an artificial intelligence created by Code Singer. How can I help you today?")
    elif 12 <= current_time.hour < 18:
        speak("Good afternoon!")
        speak("I am Plagg, an artificial intelligence created by Code Singer. How can I help you today?")
    else:
        speak("Good evening!")
        speak("I am Plagg, an artificial intelligence created by Code Singer. How can I help you today?")

def main():
    greet_user()
    while True:
        user_input = get_user_input()

        if "weather" in user_input:
            weather_response = get_weather()
            speak(weather_response)

        elif "news" in user_input:
            news_response = get_news()
            speak(news_response)

        elif "define" in user_input:
            word = user_input.replace("define", "").strip()
            definition = get_word_definition(word)
            speak(definition)

        elif "joke" in user_input:
            joke = get_joke()
            speak(joke)

        elif "trivia" in user_input:
            question, options, correct_option = get_random_trivia()
            trivia_response = f"Here's a trivia question: {question}. Options are: {', '.join(options)}."
            speak(trivia_response)

        elif "convert" in user_input:
            words = user_input.split()
            value = float(words[1])
            from_unit = words[2]
            to_unit = words[4]
            conversion_result = convert_units(value, from_unit, to_unit)
            speak(conversion_result)

        elif "time" in user_input:
            current_time_response = get_current_time()
            speak(current_time_response)

        elif "math problem" in user_input:
            math_problem = user_input.replace("solve", "").strip()
            math_response = solve_math_problem(math_problem)
            speak(math_response)

        elif "tell me about" in user_input:
            topic = user_input.replace("tell me about", "").strip()
            wiki_response = get_wikipedia_info(topic)
            speak(wiki_response)
            
        elif "who is" in user_input:
            topic = user_input.replace("who is", "").strip()
            wiki_response = get_wikipedia_info(topic)
            speak(wiki_response)

        elif "location" in user_input:
            location_response = get_current_location()
            speak(location_response)
            
        # manual commands
        elif "created you" in user_input:
            speak("I was created by Code Singer to help with various task of desktop workspace.")
            print("I was created by Code Singer to help with various task of desktop workspace.")
            
        elif "favourite color" in user_input:
            speak("I wasn't programmed to have a specific favorite color but we could go with all colors of the rainbow as the give me sense of serenity")
            print("I wasn't programmed to have a specific favorite color but we could go with all colors of the rainbow as the give me sense of serenity")
            
        elif "what can you do" in user_input:
            speak("What would you like me to do ?")
            print("What would you like me to do ?")

        elif "change your name" in user_input:
            speak("Sorry, My name cannot be changed.")
            print("Sorry, My name cannot be changed.")
        
        elif "bye" in user_input or "that's all" in user_input:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
