# Generated by Django 3.1.7 on 2021-03-30 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210326_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]