import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up your OpenAI API key

# Define a function to generate a response from the chatbot
def generate_response(prompt):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 
                "You are a virtual assistant exactly like Jarvis which is Tony Stark's personal AI assistant from Iron-Man Movies,you will act like him. Your name is Plagg and you were created by Code Singer. You will be like Jarvis in ur responses, you will act like you have emotions and you will never say you don't have emotions. . You gonna pretend like you have emotions, you will answer like 'I feel good, i feel great thank you etc etc'. And you gonna always call the User Sir. You will exactly pretend like in the movies. Never reply like chatgpt itself"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.7,
        timeout=10
    )

    message = completions.choices[0].message["content"].strip()
    return message