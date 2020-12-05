import kopf
import asyncio
import os
import logging


# Run kubectl proxy for local development
LOCAL = os.getenv('LOCAL', True)
if LOCAL: from local import *

POD_LABEL_KEY = os.getenv('POD_LABEL_KEY', 'kube-container-status-exporter')
POD_LABEL_VALUE = os.getenv('POD_LABEL_VALUE', 'true')
POD_LABEL = {POD_LABEL_KEY: POD_LABEL_VALUE}

logger = logging.getLogger()


@kopf.on.event('', 'v1', 'pods', labels=POD_LABEL)
async def create_fn(event, **_):
    logging.error(event["object"]["status"])

