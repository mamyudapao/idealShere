# Generated by Django 3.1.5 on 2021-03-09 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_auto_20210308_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
