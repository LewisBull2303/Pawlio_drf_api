# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Profile(models.Model):
    """
    A class for the user profile model
    Each user has one profile, linked via a one-to-one relationship.
    Auto creates via a signal when a new user is created.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/",
        default="Default_pfp_b2wp2a"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
