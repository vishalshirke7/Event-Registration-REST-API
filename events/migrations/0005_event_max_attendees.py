# Generated by Django 2.1.3 on 2018-11-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20181130_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='max_attendees',
            field=models.IntegerField(default=50),
        ),
    ]