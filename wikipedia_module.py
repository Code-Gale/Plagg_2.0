import wikipedia

def get_wikipedia_info(topic):
    try:
        page = wikipedia.page(topic)
        summary = wikipedia.summary(topic)
        wiki_response = f"Here is some information about {topic}: {summary}"
    except wikipedia.exceptions.PageError:
        wiki_response = f"Sorry, I couldn't find information about {topic}."
    return wiki_response
