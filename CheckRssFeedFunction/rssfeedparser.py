import feedparser
import os
from datetime import datetime
from datetime import timedelta

rssEndpoint = os.getenv("RssFeedEndpoint")

def get_latest_posts(now, last_checked):
    result = []
    feed = feedparser.parse(rssEndpoint)

    for entry in feed.entries:
        entryTime = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
        if entryTime > last_checked:
            result.append(entry)

    return result
