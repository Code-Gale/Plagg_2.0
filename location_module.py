import requests

def get_current_location():
    location_api_url = "YOUR_LOCATION_API_URL"
    try:
        response = requests.get(location_api_url)
        response.raise_for_status()
        location_data = response.json()
        current_location = location_data.get("city", "Unknown City")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching location: {e}")
        current_location = "Unknown City"
    return current_location
