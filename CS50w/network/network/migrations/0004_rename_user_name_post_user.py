# Generated by Django 3.2.4 on 2021-06-27 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_rename_user_post_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_name',
            new_name='user',
        ),
    ]