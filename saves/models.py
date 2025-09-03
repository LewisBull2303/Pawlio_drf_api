from django.db import models
from django.contrib.auth.models import User

class Saves(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'post')
        ordering = ['-saved_at']

    def __str__(self):
        return f'{self.owner.username} saved {self.post.title}'