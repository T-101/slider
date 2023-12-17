from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from slider.api.v1.serializers import PictureSerializer
from slider.models import Picture


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Picture.objects.filter(visible=True)
