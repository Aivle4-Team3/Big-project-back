# Generated by Django 5.0 on 2024-01-03 23:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0003_remove_message_lecture_message_video"),
        ("lecture", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="video",
        ),
        migrations.CreateModel(
            name="UserAndVideoRelation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="chat.message"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lecture.video"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="message",
            name="user_and_video",
            field=models.ManyToManyField(
                related_name="messages", to="chat.userandvideorelation"
            ),
        ),
    ]
