from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Saves
from .serializers import SaveSerializer

# Create your views here.
class SaveList(generics.ListCreateAPIView):
    """
    A class for listing and creating saves
    """
    serializer_class = SaveSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Saves.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'created_at',
    ]
    search_fields = [
        'owner__username',
        'post__owner__username',
        'post__category'
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'post__likes__owner__profile',
        'owner__profile',
        'post__category'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)