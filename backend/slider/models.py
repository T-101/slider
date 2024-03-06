import os
from io import BytesIO

from PIL import Image
from django.core.cache import cache

from django.core.files.base import ContentFile
from django.db import models, IntegrityError
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel
from solo.models import SingletonModel


class Settings(SingletonModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    default_visibility = models.BooleanField(default=True)
    uploads_enabled = models.BooleanField(default=True)

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    @classmethod
    def clear_cache(cls):
        cache.delete(cls.__name__)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            try:
                obj = cls.objects.create(title="Title", description="Description", default_visibility=False)
            except IntegrityError:
                obj = cls.objects.get()
            obj.set_cache()
        return cache.get(cls.__name__)

    def __str__(self):
        return self.title


class Picture(TimeStampedModel):
    file = models.ImageField(max_length=255)
    author = models.CharField(max_length=255)
    visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.file:
            img = Image.open(self.file)
            # Convert the image to WebP format
            if img.format != 'WEBP':
                buffer = BytesIO()
                img.save(buffer, format='WEBP')
                self.file.save(
                    f"{os.path.splitext(self.file.name)[0]}.webp",
                    ContentFile(buffer.getvalue()),
                    save=False
                )

        if not Settings.load().default_visibility and not self.pk:
            self.visible = False

        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Picture)
def delete_entry_files(sender, instance, **kwargs):
    try:
        os.remove(instance.file.path)
    except FileNotFoundError:
        pass
