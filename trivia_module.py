import requests

def get_random_trivia():
    trivia_api_url = "YOUR_TRIVIA_API_URL"
    response = requests.get("https://the-trivia-api.com/v2/questions")
    trivia_data = response.json()
    trivia_question = trivia_data.get("question", "I couldn't find a trivia question right now.")
    return trivia_question
