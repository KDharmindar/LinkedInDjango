# Generated by Django 2.0.5 on 2018-05-15 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_merge_20180515_0523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkedinuser',
            name='is_pin_needed',
        ),
        migrations.RemoveField(
            model_name='linkedinuser',
            name='pin',
        ),
    ]
