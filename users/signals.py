from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from nursery.models import Nursery

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    print("HJBJHBJHB")
    if created:
        if instance.user_type == "nursery":
            Nursery.objects.create(owner=instance)