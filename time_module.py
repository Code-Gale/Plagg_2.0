from datetime import datetime

def get_current_time():
    current_time = datetime.now().strftime("%I:%M %p")
    time_response = f"The current time is {current_time}."
    return time_response
