import schedule
import time

def set_reminder(message, timestamp):
    current_timestamp = time.time()
    if timestamp > current_timestamp:
        time_remaining = timestamp - current_timestamp
        schedule.every(time_remaining).seconds.do(lambda: print(f"Reminder: {message}"))
        reminder_response = f"Reminder set: {message} at {time.ctime(timestamp)}."
    else:
        reminder_response = "Please provide a valid future timestamp for the reminder."
    return reminder_response
