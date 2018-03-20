# Generated by Django 2.0.3 on 2018-03-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='favoriteproduct',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.DeleteModel(
            name='FavoriteProduct',
        ),
    ]
