import requests

def get_joke():
    joke_api_url = "YOUR_JOKE_API_URL"
    response = requests.get(joke_api_url)
    joke_data = response.json()
    joke = joke_data.get("joke", "I couldn't find a joke right now.")
    return joke
