# Generated by Django 4.1 on 2022-08-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_post_phone_post_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone_num',
            field=models.CharField(max_length=13),
        ),
    ]