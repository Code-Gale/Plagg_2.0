import requests

def get_weather(lagos):
    # Replace 'YOUR_WEATHER_API_KEY' with your actual weather API key
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={lagos}&appid=410647ae3077f684f20832176359f951"
    response = requests.get(weather_api_url)
    weather_data = response.json()

    if weather_data.get("cod") == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        weather_response = f"The weather in {lagos} is {description} with a temperature of {temperature}°C."
    else:
        weather_response = f"Sorry, I couldn't fetch weather information for {lagos}."

    return weather_response
