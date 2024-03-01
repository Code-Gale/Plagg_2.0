import requests

NEWS_API_URL = "https://newsapi.org/v2/top-headlines?country=ng&apiKey=6500379f31a9461cbe2f29c133fdd085"

def get_news():
    response = requests.get(NEWS_API_URL)
    news_data = response.json()
    top_news = news_data.get("articles", [])[:5]
    news_headlines = [news["title"] for news in top_news]
    return news_headlines

def get_news_details(news_index):
    response = requests.get(NEWS_API_URL)
    news_data = response.json()
    top_news = news_data.get("articles", [])[:5]
    selected_news = top_news[news_index]
    news_title = selected_news.get("title")
    news_description = selected_news.get("description")
    news_content = selected_news.get("content")
    return f"Title: {news_title}\nDescription: {news_description}\nContent: {news_content}"

