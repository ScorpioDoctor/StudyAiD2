# Generated by Django 2.0.10 on 2019-02-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='taxonomies.Tag', verbose_name='文章标签'),
        ),
    ]
