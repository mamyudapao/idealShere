# Generated by Django 3.1.5 on 2021-04-05 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0039_notification_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
