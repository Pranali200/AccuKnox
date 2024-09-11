"""Yes, by default, Django signals run in the same database transaction as the caller. This means
that if an operation is part of a transaction, the signal handlers triggered by that operation
will also be part of the same transaction.
This steps
1. Create a custom signal receiver that modifies the database.
2. Wrap the main operation in a transaction.
3. Raise an exception after the signal handler runs to trigger a rollback.
4. Check if the signal's changes persist."""


from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Signal receiver
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received. Modifying database...")
    instance.username = "signal_modified_username"
    instance.save()
# Function to create a user and trigger
def create_user_and_trigger_exception():
    try:
        with transaction.atomic():
            print("Transaction started. Creating user...")
            user = User.objects.create(username='test_user')
# After the signal runs, raise an exception
            print("Raising an exception to trigger rollback...")
            raise Exception("Intentional Exception to rollback transaction")
    except Exception as e:
        print(f"Exception caught: {e}")
# Run

create_user_and_trigger_exception()


try:
    user = User.objects.get(username='signal_modified_username')
    print(f"User found in database: {user.username}")
except ObjectDoesNotExist:
    print("User not found. Transaction was rolled back.")

"""Output:
Transaction started. Creating user...
Signal received. Modifying database...
Raising an exception to trigger rollback...
Exception caught: Intentional Exception to rollback transaction
User not found. Transaction was rolled back.

This demonstrates that Django signals, by default, run within the same database transaction
as the caller. If the transaction is rolled back, the changes made by the signal handler will
also be rolled back. """