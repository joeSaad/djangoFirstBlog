# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(default=datetime.date(2015, 5, 7)),
            preserve_default=False,
        ),
    ]
