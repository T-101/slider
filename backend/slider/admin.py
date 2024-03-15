from django.contrib import admin
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin

from .models import Picture, Settings


@admin.register(Settings)
class SettingsAdmin(SingletonModelAdmin):
    list_display = ['id', 'title', 'default_visibility']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'list_preview', 'visible', 'created']
    date_hierarchy = 'created'
    list_filter = ['created', 'visible']
    list_editable = ["visible"]
    search_fields = ['author']

    readonly_fields = ['image_preview']

    def list_preview(self, obj):
        try:
            return mark_safe(f'<img src="{obj.file.url}" width="100" />')
        except ValueError:
            return ""

    list_preview.short_description = 'Picture'

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width="100" />')

    image_preview.short_description = 'Picture'
