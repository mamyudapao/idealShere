# Generated by Django 3.1.5 on 2021-04-29 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0042_chat_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
    ]
