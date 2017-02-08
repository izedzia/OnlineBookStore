# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_Name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('book_logo', models.CharField(max_length=250)),
                ('book_desc', models.CharField(max_length=400)),
                ('publish_date', models.DateField()),
                ('book_price', models.CharField(default=b'100', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='book_genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storefront.Genres'),
        ),
        migrations.AddField(
            model_name='books',
            name='book_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storefront.Languages'),
        ),
    ]
