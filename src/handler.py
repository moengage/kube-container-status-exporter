import kopf
import asyncio
import os
import logging


# Run kubectl proxy for local development
LOCAL = os.getenv('LOCAL', 'true')
if LOCAL == 'true': from local import *

POD_LABEL_KEY = os.getenv('POD_LABEL_KEY')
POD_LABEL_VALUE = os.getenv('POD_LABEL_VALUE')
if POD_LABEL_KEY and POD_LABEL_VALUE:
    POD_LABEL = {POD_LABEL_KEY: POD_LABEL_VALUE}
else:
    POD_LABEL = {}

logger = logging.getLogger()


@kopf.on.event('', 'v1', 'pods', labels=POD_LABEL)
async def create_fn(event, **_):
    data = event["object"]["status"]
    data["metadata"] = {}
    data["metadata"]["name"] = event["object"]["metadata"]["name"]
    data["metadata"]["creationTimestamp"] =  event["object"]["metadata"]["creationTimestamp"]
    data["metadata"]["namespace"] = event["object"]["metadata"]["namespace"]
    data["metadata"]["labels"] = event["object"]["metadata"].get("labels")
    data["metadata"]["annotations"] = event["object"]["metadata"].get("annotations")
    logging.error(data)

