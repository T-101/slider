from rest_framework.routers import SimpleRouter

from slider.api.v1.viewsets import PictureViewSet, UploadToggleViewSet

router = SimpleRouter()

router.register('picture', PictureViewSet, basename="picture")
router.register('set_upload', UploadToggleViewSet, basename="set_upload")
