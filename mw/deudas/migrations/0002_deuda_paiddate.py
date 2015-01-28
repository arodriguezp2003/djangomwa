# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('deudas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deuda',
            name='paiddate',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 16, 35, 50, 690431, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
