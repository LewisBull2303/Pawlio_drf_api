from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        # Check image height, width and size
        from PIL import Image
        import io

        # Open the image file
        image = Image.open(value)

        if image.height > 4096:
            raise serializers.ValidationError('Your image exceeds the height limit of 4096px.')

        if image.width > 4096:
            raise serializers.ValidationError('Your image exceeds the width limit of 4096px.')

        # File size in bytes
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Your image is too large. Max size is 2MB.')

        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user

        image = validated_data.pop('image', None)
        post = Post.objects.create(**validated_data)

        if image:
            post.image = image
            post.save()

        return post

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'category',
            'title',
            'content',
            'image',
            'like_id',
            'comments_count',
            'likes_count',
        ]