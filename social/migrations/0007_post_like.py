# Generated by Django 4.0.5 on 2022-07-05 03:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0006_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='social_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
