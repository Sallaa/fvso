from app import CONFIG, app
from .models import *
from newspaper import Article
from newsapi import NewsApiClient

news_api = NewsApiClient(CONFIG["NEWS_API_KEY"])

def parse_url(url):
    article = Article(url)
    article.download()
    article.parse()
    # article.nlp()
    data = {"title": article.title, "author": article.authors, "date": article.publish_date, "img": article.top_image, "tags": article.keywords}

    return data

