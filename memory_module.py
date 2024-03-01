# memory.py
import json
from datetime import datetime

MEMORY_FILE = 'conversation_memory.json'

def load_conversation_history():
    try:
        with open(MEMORY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_conversation_history(history):
    with open(MEMORY_FILE, 'w') as file:
        json.dump(history, file)

def update_conversation_history(user_input, plagg_response):
    history = load_conversation_history()
    timestamp = str(datetime.now())
    history[timestamp] = {'user_input': user_input, 'plagg_response': plagg_response}
    save_conversation_history(history)

def get_last_user_input():
    history = load_conversation_history()
    if history:
        timestamps = sorted(history.keys(), reverse=True)
        last_timestamp = timestamps[0]
        return history[last_timestamp]['user_input']
    return None

def search_memory(query):
    history = load_conversation_history()
    matched_entries = []
    for timestamp, entry in history.items():
        if query.lower() in entry['user_input'].lower():
            matched_entries.append((timestamp, entry))
    return matched_entries

def find_last_occurrence(query):
    history = load_conversation_history()
    for timestamp in sorted(history.keys(), reverse=True):
        if query.lower() in history[timestamp]['user_input'].lower():
            return history[timestamp]
    return None
