import datetime
import logging
import azure.functions as func
from . import tinyurl as tinyurl_service
from . import rssfeedparser


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    latest_posts = rssfeedparser.get_latest_posts()
    tinyurl_service.send_updates(latest_posts)
