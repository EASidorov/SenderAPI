from .models import *

def show_stats():
    clients = len(Client.objects.all())
    dispatches = len(Dispatch.objects.all())
    messages = len(Message.objects.all())

    sent_msgs = len([msg for msg in messages if msg.status == 'Отправлено'])

    response = {
        'Клиенты': clients,
        'Рассылки': dispatches,
        'Сообщения': messages,
        'Отправленые сообщения': sent_msgs,
    }

    return response