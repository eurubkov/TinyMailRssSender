import logging 
import os
import tinyapi

username = os.getenv("TinyUrlUsername")
password  = os.getenv("TinyUrlPassword")
rssEndpoint = os.getenv("RssFeedEndpoint")

session = tinyapi.Session(username, password)

def send_updates():
    draft = session.create_draft()
    draft.subject = "Testing tiny api"
    draft.body = "Content should be here"
    draft.save()

    draft.send_preview()