# Generated by Django 5.1.4 on 2025-01-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers', '0002_remove_newspaper_topic_newspaper_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspaper',
            old_name='topic',
            new_name='topics',
        ),
    ]
