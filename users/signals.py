from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
import time

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal triggered at: {timezone.now()}")  # Log the time when signal is triggered
    time.sleep(5)  # Simulate long-running operation
    print("Signal handler finished execution")
