# Generated by Django 3.1.7 on 2021-03-25 21:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='teste'),
            preserve_default=False,
        ),
    ]