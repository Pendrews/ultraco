# Generated by Django 4.1.3 on 2022-12-20 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_rename_first_name_beneficiary_b_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiary',
            old_name='b_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='beneficiary',
            old_name='b_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='beneficiary',
            old_name='b_user',
            new_name='user',
        ),
    ]
