# Generated by Django 2.0.3 on 2018-03-21 15:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0021_auto_20180321_1325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follow',
            new_name='FollowUser',
        ),
    ]
