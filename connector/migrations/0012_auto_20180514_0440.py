# Generated by Django 2.0.5 on 2018-05-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0011_auto_20180513_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskqueue',
            name='status',
            field=models.CharField(choices=[('Queued', 'Queued'), ('Running', 'Running'), ('Pin Required', 'Pin Required'), ('Pin Checking', 'Pin Checking'), ('Pin Invalid', 'Pin Invalid'), ('Error', 'Error'), ('Done', 'Done')], default='Queued', max_length=10),
        ),
    ]
