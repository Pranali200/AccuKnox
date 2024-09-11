"""By default, Django signals are executed synchronously. This means that when a signal is sent,
all connected receivers are called and executed in the same thread and process, immediately
before the flow of the program continues."""

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver function
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received! Starting to process...")
    time.sleep(5) # Simulate a time-consuming task
    print("Signal processing completed.")

# new user instance to trigger the signal
user = User.objects.create(username='test_user')
print("User creation completed.")

"""Output:
Signal received! Starting to process...
Signal processing completed.
User creation completed."""

"""The my_signal_receiver function is connected to the post_save signal of the User model.
This function simulates a time-consuming task using time.sleep(5).

 When a new User is created with User.objects.create(username='test_user'), the
post_save signal is sent.
 "User creation completed." message does not print until after the signal processing
completes. This confirms that the signal was processed synchronously, blocking further
execution of code until the signal receiver finishes its work."""