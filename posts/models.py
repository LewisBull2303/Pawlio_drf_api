from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    category_choices = [
        ('Puppy', 'Puppy'),
        ('Senior Dog', 'Senior Dog'),
        ('Nature', 'Nature'),
        ('Family', 'Family'),
        ('Big Dog', 'Big Dog'),
        ('Small Dog', 'Small Dog'),
        ('Funny', 'Funny'),
        ('Sleeping', 'Sleeping'),
        ('Playing', 'Playing'),
        ('Zoomies', 'Zoomies'),
        ('Camping', 'Camping'),
        ('Kids & Dogs', 'Kids & Dogs'),
        ('Cute', 'Cute'),
        ('Silly', 'Silly')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='default_post_wbup9c', blank=True
    )
    category = models.CharField(max_length=50, choices=category_choices)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'