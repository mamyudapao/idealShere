# Generated by Django 3.1.5 on 2021-02-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20210223_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='sample.jpg', upload_to='api/posts'),
            preserve_default=False,
        ),
    ]
