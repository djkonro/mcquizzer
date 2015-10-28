# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.AddField(
            model_name='quiz',
            name='question',
            field=models.ForeignKey(default=1, to='quizer.Question'),
            preserve_default=False,
        ),
    ]
