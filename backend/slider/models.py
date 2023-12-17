import os
from io import BytesIO

from PIL import Image

from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel


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

        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Picture)
def delete_entry_files(sender, instance, **kwargs):
    try:
        os.remove(instance.file.path)
    except FileNotFoundError:
        pass
