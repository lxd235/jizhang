# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 03:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(verbose_name='\u7535\u8bdd')),
                ('level', models.IntegerField(verbose_name='\u7b49\u7ea7')),
                ('image', models.ImageField(max_length=150, upload_to=b'', verbose_name='\u5934\u50cf')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-write_date']},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='p_catagory',
            new_name='p_category',
        ),
    ]
