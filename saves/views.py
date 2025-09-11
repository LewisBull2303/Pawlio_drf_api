# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from saves.models import Save
from saves.serializer import SaveSerializer

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class SaveList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer

    def get_queryset(self):
        return Save.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class SaveDetail(generics.RetrieveDestroyAPIView):
    """
    a class for the save details
    Users can retrieve a save or remove a saved post
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()


class UserSaveList(generics.ListAPIView):
    """
    a class for the user's saved posts
    """
    serializer_class = SaveSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Save.objects.filter(owner=self.request.user)
