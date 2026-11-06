from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from slider.api.v1.serializers import PictureSerializer, PictureVisibilitySerializer
from slider.models import Picture, Settings


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Picture.objects.filter(visible=True)


class PictureVisibilityViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = PictureVisibilitySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Picture.objects.order_by('-created')
        visible = self.request.query_params.get('visible')
        if visible is not None:
            queryset = queryset.filter(visible=visible.lower() == 'true')
        return queryset


class UploadToggleViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    def create(self, request):
        if type(request.data) is not bool:
            return Response(status=400, data={"error": "Invalid request"})
        settings = Settings.load()
        settings.uploads_enabled = request.data
        settings.save()
        return Response(status=200, data={"uploads_enabled": Settings.load().uploads_enabled})
