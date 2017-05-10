# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-21 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cleaners', '0002_cities'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('cleaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaners.Cleaner')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
    ]
