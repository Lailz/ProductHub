# Generated by Django 2.0.3 on 2018-03-21 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20180321_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
    ]