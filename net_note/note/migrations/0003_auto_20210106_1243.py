# Generated by Django 2.2.12 on 2021-01-06 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20210106_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='user_id',
        ),
    ]
