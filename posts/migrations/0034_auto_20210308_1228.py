# Generated by Django 3.1.5 on 2021-03-08 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20210308_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
