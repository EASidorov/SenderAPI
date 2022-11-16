from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import datetime, timedelta
from threading import Timer

from .models import *
from .sender import *

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Client)
def client_log(created, instance, **kwargs):
    if created:
        logger.info(f'Создан клиент')

@receiver(post_save, sender=Dispatch)
def dispatch_log(created, instance, **kwargs):
    if created:
        time_delta = instance.start_dt-datetime.now()
        if time_delta > 0:
            t = Timer(time_delta, select_target(instance))
            t.start()
        else:
            select_target(instance)

