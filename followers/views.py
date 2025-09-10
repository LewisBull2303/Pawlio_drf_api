# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Follower
from .serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FollowerList(generics.ListCreateAPIView):
    """
    A class for the follower list view
    """
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    A class for Follower details
    User can retrieve a follower or unfollow someone
    """
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
