# Generated by Django 4.1.3 on 2022-12-06 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account',
        ),
    ]
