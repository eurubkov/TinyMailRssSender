import datetime
from datetime import timedelta
import logging
import azure.functions as func
from . import tinyurl as tinyurl_service
from . import rssfeedparser
from . import storageservice


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    now = datetime.datetime.utcnow()
    last_checked = storageservice.get_checkpoint_datetime()
    if last_checked == None:
        last_checked = datetime.utcnow + timedelta(hours=-1)
    latest_posts = rssfeedparser.get_latest_posts(now, last_checked)
    tinyurl_service.send_updates(latest_posts)
    storageservice.create_or_update_blob(now)
    