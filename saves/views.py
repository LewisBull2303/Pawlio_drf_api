from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from saves.models import Save
from saves.serializer import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

class UserSaveList(generics.ListAPIView):
    serializer_class = SaveSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Save.objects.filter(owner=self.request.user)
