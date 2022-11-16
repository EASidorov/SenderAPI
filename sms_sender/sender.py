import environ
import requests
import logging

from .models import *


logger = logging.getLogger(__name__)
env = environ.Env()
environ.Env.read_env()

URL = 'https://probe.fbrq.cloud/v1/send'
TOKEN = env("API_TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def select_target(dispatch):
    tags = dispatch.tags.all()
    operators = dispatch.operators.all()
    clients = Client.objects.all()
    targets = [client for client in clients if (client.tag in tags) or (client.operator_code in operators)]
    logger.log(f'Найдено целей {len(targets)}')
    for t in targets:
        send(t, dispatch)


def send(client, dispatch):
    new_msg = Message(client_id=client.id, dispatch_id=dispatch.id)
    new_msg.save()
    body = {
        "id": new_msg.id,
        "phone": client.p_number,
        "text": dispatch.text
    }
    response = requests.post(
        url=f'{URL}{new_msg.id}',
        headers=HEADERS,
        json=body,
        timeout=5
    )
    logger.log(response)


