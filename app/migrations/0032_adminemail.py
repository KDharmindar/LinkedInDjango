# Generated by Django 2.0.5 on 2018-06-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20180531_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=70)),
            ],
        ),
    ]