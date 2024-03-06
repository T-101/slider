from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from slider.api.v1.serializers import PictureSerializer
from slider.models import Picture, Settings


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Picture.objects.filter(visible=True)


class UploadToggleViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    def create(self, request):
        if type(request.data) is not bool:
            return Response(status=400, data={"error": "Invalid request"})
        settings = Settings.load()
        settings.uploads_enabled = request.data
        settings.save()
        return Response(status=200, data={"uploads_enabled": Settings.load().uploads_enabled})
