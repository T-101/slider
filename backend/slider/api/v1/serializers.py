from rest_framework.serializers import ModelSerializer

from slider.models import Picture


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        exclude = ['modified']
