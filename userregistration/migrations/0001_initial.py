# Generated by Django 2.1.3 on 2018-11-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('number', models.IntegerField(unique=True)),
            ],
        ),
    ]
