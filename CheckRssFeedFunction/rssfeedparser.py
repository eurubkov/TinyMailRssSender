import feedparser
import os
from datetime import datetime
from datetime import timedelta

rssEndpoint = os.getenv("RssFeedEndpoint")

def get_latest_posts():
    result = []
    now = datetime.utcnow()
    feed = feedparser.parse(rssEndpoint)

    for entry in feed.entries:
        entryTime = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
        if entryTime > now + timedelta(days=-2):
            print(entryTime)
            print(now + timedelta(days=-1))
            result.append(entry)

    return result
