import requests

def get_current_location():
    location_api_url = "YOUR_LOCATION_API_URL"
    response = requests.get(location_api_url)
    location_data = response.json()
    current_location = location_data.get("city", "Unknown City")
    return current_location
