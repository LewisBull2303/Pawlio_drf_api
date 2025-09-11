# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Post(models.Model):
    """
    A class for the post model
    """
    category_choices = [
        ("Dog", "Dog"),
        ("Puppy", "Puppy"),
        ("Old Pet", "Old Pet"),
        ("Nature", "Nature"),
        ("Family", "Family"),
        ("Big Pet", "Big Pet"),
        ("Small Pet", "Small Pet"),
        ("Funny", "Funny"),
        ("Sleeping", "Sleeping"),
        ("Playing", "Playing"),
        ("Zoomies", "Zoomies"),
        ("Camping", "Camping"),
        ("Kids & Pets", "Kids & Pets"),
        ("Cute", "Cute"),
        ("Silly", "Silly"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=1000)
    category = models.CharField(
        max_length=50, choices=category_choices, default="Dog"
    )
    image = models.ImageField(
        upload_to="images/", default="default_post_wbup9c", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.id} {self.title}"
