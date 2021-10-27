from django.db.models.signals import post_save
from django.dispatch import receiver

from newsboard.models import Comment


@receiver(post_save, sender=Comment)
def send_mail(sender, instance, created, **kwargs):
    if not created:
        pass