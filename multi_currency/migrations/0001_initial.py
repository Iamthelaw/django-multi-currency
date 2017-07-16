# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='For example: USD, EUR, RUB', unique=True, max_length=3, verbose_name='Currency code')),
                ('rate', models.FloatField(default=0, verbose_name='Currency rate')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
            ],
            options={
                'ordering': ('code', 'last_modified'),
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
    ]
