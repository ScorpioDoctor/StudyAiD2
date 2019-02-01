# Generated by Django 2.0.10 on 2019-02-01 19:11

import articles.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(articles.models.get_sentinel_user), to=settings.AUTH_USER_MODEL, verbose_name='文章作者'),
        ),
    ]