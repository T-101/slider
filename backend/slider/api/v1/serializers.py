from rest_framework.serializers import ModelSerializer, SerializerMethodField

from slider.models import Picture


class PictureSerializer(ModelSerializer):
    url = SerializerMethodField()

    class Meta:
        model = Picture
        exclude = ['modified', 'visible']

    def get_url(self, obj):
        return obj.file.url


class PictureVisibilitySerializer(ModelSerializer):
    url = SerializerMethodField()

    class Meta:
        model = Picture
        fields = ['id', 'url', 'author', 'created', 'visible']
        read_only_fields = ['id', 'url', 'author', 'created']

    def get_url(self, obj):
        return obj.file.url
