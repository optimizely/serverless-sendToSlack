'''
This has been customized from the original version in AWS Lambda's pre-made script library.

Follow these steps to configure the webhook in Slack:

  1. Navigate to https://<your-team-domain>.slack.com/services/new

  2. Search for and select "Incoming WebHooks".

  3. Choose the default channel where messages will be sent and click "Add Incoming WebHooks Integration".

  4. Copy the webhook URL from the setup instructions and use it in the next section.
'''
from __future__ import print_function

import os
import sys

# Only load linux-compiled dependencies if executing under linux
if sys.platform.startswith('linux'):
  here = os.path.dirname(os.path.realpath(__file__))
  sys.path.append(os.path.join(here, "vendored"))

import boto3
import datetime
import json
import logging

from envparse import env
from urllib2 import Request, urlopen, URLError, HTTPError

# The Slack channel to send a message to stored in the slackChannel environment variable
SLACK_CHANNEL = env('SLACK_CHANNEL')
HOOK_URL = env('SLACK_HOOK_URL')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# JSON doesn't have a python-compatible datetime object, so we need to ensure that we can parse dates without errors.
json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)

def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    message = event['Records'][0]['Sns']['Message']
    logger.info("Message: " + str(message))

    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': "Message from AWS:\n%s" % (message)
    }

    req = Request(HOOK_URL, json.dumps(slack_message))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
