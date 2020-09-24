import logging 
import os
import tinyapi

username = os.getenv("TinyUrlUsername")
password  = os.getenv("TinyUrlPassword")

session = tinyapi.Session(username, password)

def send_updates(latest_posts):
    for post in latest_posts:
        draft = session.create_draft()
        draft.subject = post.title
        draft.body = post.link
        draft.body += post['content'].pop(0).value
        draft.save()

        draft.send()