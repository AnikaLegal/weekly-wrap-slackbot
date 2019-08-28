import requests
import logging

import secrets

logging.basicConfig(
    filename="/srv/slackbot/slackbot.log",
    filemode="a",
    format="[%(asctime)s] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
)

PROD_WEBHOOK_URL = secrets.PROD_WEBHOOK_URL
TEST_WEBHOOK_URL = secrets.TEST_WEBHOOK_URL
WEBHOOK_URL = PROD_WEBHOOK_URL  # WARNING - THIS WILL ANNOY PEOPLE
HEADERS = {"Content-Type": "application/json"}
TEXT = """
Hi <!channel>!

It's time for your Weekly Wrap status update. If you did anything Anika related this week, then you should share it with the rest of the team.
This is important to keep everybody in the loop about what's going on and boost morale.

Please send a message to Kathryn Quinn detailing any milestones, or updates that you have to share.

:heart: Bender :robot_face:
"""

logging.info("Posting weekly wrap message")
resp = requests.post(WEBHOOK_URL, json={"text": TEXT}, headers=HEADERS)
