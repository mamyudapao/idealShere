# Generated by Django 3.1.5 on 2021-02-17 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='member',
        ),
    ]