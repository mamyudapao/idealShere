# Generated by Django 3.1.5 on 2021-03-03 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20210303_0419'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
    ]
