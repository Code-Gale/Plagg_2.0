import requests

def get_joke():
    joke_api_url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(joke_api_url)
        response.raise_for_status()
        joke_data = response.json()
        joke = joke_data.get("joke", "I couldn't find a joke right now.")
    except requests.exceptions.RequestException as e:
        joke = f"An error occurred: {str(e)}"
    return joke