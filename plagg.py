from datetime import datetime
from tts_module import speak
from weather_module import fetch_weather
from news_module import get_news, get_news_details
from time_module import get_current_time
from math_module import solve_math_problem
from wikipedia_module import get_wikipedia_info
from location_module import get_current_location
#from hmm.dictionary_module import get_word_definition
from jokes_module import get_joke
from trivia_module import get_random_trivia
from unit_conversion_module import convert_units
from speech_recognition_module import get_user_input
from openai_module import generate_response
from web_module import open_website
import json
from memory_module import load_conversation_history, save_conversation_history, update_conversation_history, get_last_user_input, search_memory, find_last_occurrence

def check_last_greeting():
    try:
        with open('last_greeting.json', 'r') as file:
            data = json.load(file)
            last_greeting_date = data.get('last_greeting_date')
            return last_greeting_date
    except FileNotFoundError:
        return None

def update_last_greeting():
    current_date = datetime.now().date()
    data = {'last_greeting_date': str(current_date)}
    with open('last_greeting.json', 'w') as file:
        json.dump(data, file)

def greet_user():
    last_greeting_date = check_last_greeting()
    current_date = datetime.now().date()
    current_time = datetime.now().time()

    if last_greeting_date == str(current_date):
        # Returning user greeting
        if current_time.hour < 12:
            alternate_greeting = "Pleased to have you back. How can I be of service once again?"
        elif 12 <= current_time.hour < 18:
            alternate_greeting = "Welcome back. How can I assist you once again?"
        else:
            alternate_greeting = "Welcome back. How can I assist you once again?"
        speak(alternate_greeting)
    else:
        # First-time user or new day greeting
        if current_time.hour < 12:
            greeting = "Good morning! It's a brand new day."
        elif 12 <= current_time.hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"
        speak(f"{greeting} I am Plagg, an artificial intelligence created by Code Singer. How can I help you today?")

        # Update the last greeting date
        update_last_greeting()


def interrupt_activity():
    # Check for user interruption
    user_input = get_user_input().lower()
    if "enough for now" in user_input or "stop" in user_input or "that's enough" in user_input:
        speak("Alright, let me know if you need anything else.")
        
def summarize_previous_conversation(query):
    matched_entries = search_memory(query)
    if matched_entries:
        speak(f"I found {len(matched_entries)} matching entries in our conversation history.")
        for timestamp, entry in matched_entries:
            speak(f"On {timestamp}, you asked: {entry['user_input']}")
            speak(f"I responded: {entry['plagg_response']}")
    else:
        speak("I couldn't find any matching entries in our conversation history.")

def handle_do_you_remember_query(query):
    result = find_last_occurrence(query)
    if result:
        speak(f"Yes, I remember. On {result['timestamp']}, you asked: {result['user_input']}")
        speak(f"I responded: {result['plagg_response']}")
    else:
        speak("I don't recall that specific conversation.")
        
def main():
    greet_user()
    while True:
        user_input = get_user_input()

        if "weather" in user_input:
            weather_response = fetch_weather()
            speak(weather_response)
            
        elif 'are you there' in user_input :
            activate = ("For you Sir, Always!")
            print(activate)
            speak(activate)

        elif "news" in user_input:
            news_response = get_news()
            speak("Here are the latest headlines:")
            for index, headline in enumerate(news_response, start=1):
                speak(f"{index}. {headline}")
                

            speak("Would you like more details on a specific news? If yes, please provide the news number.")
            user_input = get_user_input()
            try:
                news_index = int(user_input) - 1
                if 0 <= news_index < len(news_response):
                    news_details = get_news_details(news_index)
                    speak(news_details)
            except ValueError:
                pass

        elif "joke" in user_input:
            joke = get_joke()
            speak(joke)

        elif "trivia" in user_input:
            question, options, correct_option = get_random_trivia()
            trivia_response = f"Here's a trivia question: {question}. Options are: {', '.join(options)}."
            speak(trivia_response)
            # Use the correct_option variable here if needed

        elif "open YouTube and search for" in user_input or "I need videos on" in user_input:
            query = user_input.replace("open youtube and search for", "").strip()
            url = f"https://www.youtube.com/results?search_query={query}"
            response = ("Right away sir.")
            speak(response)
            open_website(url)
            

        elif "open Amazon and search for" in user_input:
            query = user_input.replace("open amazon and search for", "").strip()
            url = f"https://www.amazon.com/s?k={query}"
            open_website(url)

        elif "time" in user_input:
            current_time_response = get_current_time()
            speak(current_time_response)

        elif "math problem" in user_input:
            math_problem = user_input.replace("solve", "").strip()
            math_response = solve_math_problem(math_problem)
            speak(math_response)

        #elif "who is" in user_input:
        #    topic = user_input.replace("tell me about", "").replace("who is", "").strip()
        #    wiki_response = get_wikipedia_info(topic)
        #    speak(wiki_response)

        elif "location" in user_input:
            location_response = get_current_location()
            speak(location_response)
            
        #elif "created you" in user_input:
        #    response = "I was created by Code Singer to help with various tasks of the desktop workspace."
        #    speak(response)
        #    print(response)
            
        elif "favourite color" in user_input:
            response = "I wasn't programmed to have a specific favorite color, but we could go with all colors of the rainbow as they give me a sense of serenity."
            speak(response)
            print(response)
            
        elif "what can you do" in user_input:
            response = "What would you like me to do?"
            speak(response)
            print(response)

        elif "change your name" in user_input:
            response = "Sorry, my name cannot be changed."
            speak(response)
            print(response)
        
        elif "bye" in user_input or 'that will be all for now' in user_input:
            speak("Goodbye!")
            break
        
        elif "stop" in user_input or "enough" in user_input:
            interrupt_activity()
            
        elif "last question" in user_input:
            last_user_input = get_last_user_input()
            if last_user_input:
                speak(f"The last question you asked me was: {last_user_input}")
            else:
                speak("I don't have information about our last conversation.")
                
        elif "summarize previous conversation about" in user_input or 'summarise our last conversation about' in user_input:
            query = user_input.replace("summarize previous conversation about", "").strip()
            summarize_previous_conversation(query)
            
        elif "do you remember when I asked you about" or 'do you remember when we spoke about' in user_input:
            query = user_input.replace("do you remember when I asked you about", "").strip()
            handle_do_you_remember_query(query)
        
        else:
            openai_response = generate_response(user_input)
            speak(openai_response)
            plagg_response = generate_response(user_input)
            update_conversation_history(user_input, plagg_response)
            
        
            

if __name__ == "__main__":
    main()
