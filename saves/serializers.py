from posts.models import Post
from rest_framework import serializers
from .models import Saves

class SaveSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # <- add this
    post_id = serializers.ReadOnlyField(source='post.id')
    post_image = serializers.ReadOnlyField(source='post.image.url')
    post_owner = serializers.ReadOnlyField(source='post.owner.username')
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Saves
        fields = [
            'id',
            'owner',
            'post',
            'post_id',
            'post_image',
            'post_owner',
            'created_at',
        ]
