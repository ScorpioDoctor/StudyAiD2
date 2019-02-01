# Generated by Django 2.0.10 on 2019-02-01 19:11

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import taxonomies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxonomies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='文章标题')),
                ('brief', models.CharField(blank=True, default='这篇文章没有摘要', max_length=120, verbose_name='文章摘要')),
                ('front_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='articles/images/', verbose_name='文章封面')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章内容')),
                ('word_count', models.IntegerField(default=0, verbose_name='文章字数')),
                ('click_number', models.IntegerField(default=0, verbose_name='点击量')),
                ('favor_number', models.IntegerField(default=0, verbose_name='收藏量')),
                ('comment_number', models.IntegerField(default=0, verbose_name='评论量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(on_delete=models.SET(taxonomies.models.get_sentinel_category), to='taxonomies.Category', verbose_name='文章类别')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='taxonomies.Tag', verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
