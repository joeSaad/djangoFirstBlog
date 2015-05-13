# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='authors',
            fields=[
                ('authorName', models.CharField(max_length=40)),
                ('authorID', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='posts',
            name='author',
        ),
        migrations.AddField(
            model_name='posts',
            name='authorID',
            field=models.IntegerField(default=datetime.date(2015, 5, 12)),
            preserve_default=False,
        ),
    ]
