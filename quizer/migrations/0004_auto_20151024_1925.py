# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0003_auto_20151023_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=1, to='quizer.Quiz'),
            preserve_default=False,
        ),
    ]
