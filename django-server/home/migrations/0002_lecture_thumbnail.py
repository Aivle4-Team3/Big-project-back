# Generated by Django 3.2.23 on 2023-12-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='thumbnail',
            field=models.ImageField(default='default_thumbnail.jpg', upload_to='uploads/'),
        ),
    ]
