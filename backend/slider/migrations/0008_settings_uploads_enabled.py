# Generated by Django 5.0.2 on 2024-03-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0007_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='uploads_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
