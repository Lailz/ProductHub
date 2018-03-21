# Generated by Django 2.0.3 on 2018-03-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_remove_profile_follows'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('-follow_time',)},
        ),
        migrations.AlterField(
            model_name='follow',
            name='follow_time',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
