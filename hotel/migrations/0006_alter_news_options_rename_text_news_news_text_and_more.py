# Generated by Django 4.1 on 2022-10-20 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_news_alter_post_email_alter_post_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='text',
            new_name='news_text',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='news_title',
        ),
    ]