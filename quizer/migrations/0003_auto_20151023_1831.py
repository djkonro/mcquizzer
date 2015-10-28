# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0002_auto_20151023_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]
