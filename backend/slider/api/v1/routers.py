from rest_framework.routers import SimpleRouter

from slider.api.v1.viewsets import PictureViewSet

router = SimpleRouter()

router.register('picture', PictureViewSet, basename="picture")
