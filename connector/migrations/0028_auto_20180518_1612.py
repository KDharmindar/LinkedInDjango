# Generated by Django 2.0.5 on 2018-05-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0027_auto_20180518_1612'),
    ]

    operations = [
         migrations.AlterField(
            model_name='searchresult',
            name='linkedin_id',
            field=models.CharField(max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
