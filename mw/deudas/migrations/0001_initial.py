# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deuda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('paid', models.BooleanField(default=False, verbose_name=b'Pagado')),
                ('state', models.CharField(default=b'DEUDA', max_length=8, choices=[(b'DEUDA', b'DEUDA'), (b'PRESTAMO', b'PRESTAMO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('phone', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deuda',
            name='Persona',
            field=models.ForeignKey(to='deudas.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deuda',
            name='owner',
            field=models.ForeignKey(related_name='usuario_deuda', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
