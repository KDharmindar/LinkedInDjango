# Generated by Django 2.0.5 on 2018-05-10 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20180510_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='membership_type',
        ),
        migrations.AddField(
            model_name='membership',
            name='membership_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='membership_types', to='app.MembershipType'),
            preserve_default=False,
        ),
    ]
