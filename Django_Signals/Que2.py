"""Yes, Django signals run in the same thread as the caller. This means that the signal handler
i.e. receiver executes in the same thread that sent the signal. """

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Signal receiver function
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")
# Function to create a user and trigger the signal
def create_user():
    print(f"User creation started in thread: {threading.current_thread().name}")
    user = User.objects.create(username='test_user')
# create_user function
create_user()


"""Output:
User creation started in thread: MainThread
Signal received in thread: MainThread

This code conclusively demonstrates that Django signals are executed in the same thread as
the caller by comparing the thread names during both the signal sending and handling
processes. """