from rest_framework import serializers
from .models import Saves
from posts.models import Post

class SaveSerializer(serializers.ModelSerializer):
    """
    A class for a SaveSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post_id = serializers.ReadOnlyField(source='post.id')
    post_image = serializers.ReadOnlyField(source='post.image.url')
    post_owner = serializers.ReadOnlyField(source='post.owner.username')
    created_at = serializers.ReadOnlyField()

    def get_post_details(self, obj):
        post = Post.objects.get(id=obj.post.id)
        return {
            'id': post.id,
            'image': post.image.url,
            'owner': post.owner.username,
        }

    class Meta:
        model = Saves
        fields = [
            'id',
            'owner',
            'post_id',
            'post_image',
            'post_owner',
            'created_at',
        ]