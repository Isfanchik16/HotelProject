# Generated by Django 4.1 on 2022-08-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_post_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='phone',
        ),
        migrations.AddField(
            model_name='post',
            name='phone_num',
            field=models.CharField(default=900000000, max_length=12),
            preserve_default=False,
        ),
    ]