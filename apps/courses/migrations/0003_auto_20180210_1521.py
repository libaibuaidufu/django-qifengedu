# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='lesson_key',
        ),
        migrations.AddField(
            model_name='courses',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Education', verbose_name='学历'),
        ),
        migrations.AddField(
            model_name='courses',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Grade', verbose_name='年级'),
        ),
        migrations.AddField(
            model_name='courses',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='科目'),
        ),
    ]
