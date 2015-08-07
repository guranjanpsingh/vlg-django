# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=2000)),
                ('postedBy', models.CharField(max_length=30)),
                ('postedOn', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='commentDislikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dislikedBy', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='commentLikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likedBy', models.CharField(max_length=30)),
                ('commentsID', models.ForeignKey(to='vlg_django.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.CharField(max_length=2000)),
                ('postedOn', models.DateTimeField()),
                ('postedBy', models.CharField(max_length=30)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostDisikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dislikedBy', models.CharField(max_length=30)),
                ('postsID', models.ForeignKey(to='vlg_django.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likedBy', models.CharField(max_length=30)),
                ('postsID', models.ForeignKey(to='vlg_django.Post')),
            ],
        ),
        migrations.AddField(
            model_name='commentdislikes',
            name='commentsID',
            field=models.ForeignKey(to='vlg_django.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postsID',
            field=models.ForeignKey(to='vlg_django.Post'),
        ),
    ]
