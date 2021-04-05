# Generated by Django 3.1.5 on 2021-04-05 00:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0038_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
