from datetime import datetime
import time
from tts_module import speak_text
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
        speak_text("Good morning!")
        speak_text("I am Plagg, an artificial intelligence created by Code Singer. How can I help you today?")
    elif 12 <= current_time.hour < 18:
        speak_text("Good afternoon!")
        speak_text("I am Plagg, an artificial intelligence created by Code Singer. How can I help you today?")
    else:
        speak_text("Good evening!")
        speak_text("I am Plagg, an artificial intelligence created by Code Singer. How can I help you today?")

def main():
    greet_user()
    while True:
        user_input = get_user_input()

        if "weather" in user_input:
            weather_response = get_weather()
            speak_text(weather_response)

        elif "news" in user_input:
            news_response = get_news()
            speak_text(news_response)

        elif "define" in user_input:
            word = user_input.replace("define", "").strip()
            definition = get_word_definition(word)
            speak_text(definition)

        elif "joke" in user_input:
            joke = get_joke()
            speak_text(joke)

        elif "trivia" in user_input:
            question, options, correct_option = get_random_trivia()
            trivia_response = f"Here's a trivia question: {question}. Options are: {', '.join(options)}."
            speak_text(trivia_response)

        elif "convert" in user_input:
            words = user_input.split()
            value = float(words[1])
            from_unit = words[2]
            to_unit = words[4]
            conversion_result = convert_units(value, from_unit, to_unit)
            speak_text(conversion_result)

        elif "time" in user_input:
            current_time_response = get_current_time()
            speak_text(current_time_response)

        elif "math problem" in user_input:
            math_problem = user_input.replace("solve", "").strip()
            math_response = solve_math_problem(math_problem)
            speak_text(math_response)

        elif "tell me about" in user_input:
            topic = user_input.replace("tell me about", "").strip()
            wiki_response = get_wikipedia_info(topic)
            speak_text(wiki_response)
            
        elif "who is" in user_input:
            topic = user_input.replace("who is", "").strip()
            wiki_response = get_wikipedia_info(topic)
            speak_text(wiki_response)

        elif "location" in user_input:
            location_response = get_current_location()
            speak_text(location_response)

        elif "bye" in user_input or "that's all" in user_input:
            speak_text("Goodbye!")
            break

        else:
            speak_text("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()