# Generated by Django 3.1.5 on 2021-03-11 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='introduction',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
