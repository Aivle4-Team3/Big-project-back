# Generated by Django 5.0 on 2024-01-08 08:34

import config.asset_storage
import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Enrollment",
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
                ("playback_duration", models.DurationField(default=datetime.timedelta)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enrollments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lecture",
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
                ("title", models.CharField(default="", max_length=100)),
                ("title_info", models.CharField(default="", max_length=1000)),
                ("subject", models.CharField(default="", max_length=10)),
                (
                    "thumbnail",
                    models.ImageField(
                        default="default_thumbnail.jpg",
                        storage=config.asset_storage.MediaStorage(),
                        upload_to="images/",
                    ),
                ),
                ("summary", models.TextField(default="")),
                ("student_count", models.IntegerField(default=0)),
                (
                    "rating",
                    models.SmallIntegerField(
                        default=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("remain_time", models.DurationField(default=datetime.timedelta)),
                (
                    "teacher",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"groups__name": "선생"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="lectures",
                        through="lecture.Enrollment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="enrollment",
            name="lecture",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrollments",
                to="lecture.lecture",
            ),
        ),
        migrations.CreateModel(
            name="Video",
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
                ("name", models.CharField(max_length=100)),
                (
                    "file",
                    models.FileField(
                        null=True,
                        storage=config.asset_storage.MediaStorage(),
                        upload_to="videos/",
                        verbose_name="",
                    ),
                ),
                ("video_duration", models.DurationField(default=datetime.timedelta)),
                (
                    "lecture",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="lecture.lecture",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="enrollment",
            unique_together={("user", "lecture")},
        ),
    ]
