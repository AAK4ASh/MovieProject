# Generated by Django 4.2.6 on 2023-10-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_alter_movie_desc_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='image', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
