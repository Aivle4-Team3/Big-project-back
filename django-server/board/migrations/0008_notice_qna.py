# Generated by Django 5.0 on 2024-01-07 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0007_alter_post_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                (
                    "post_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="board.post",
                    ),
                ),
            ],
            bases=("board.post",),
        ),
        migrations.CreateModel(
            name="QnA",
            fields=[
                (
                    "post_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="board.post",
                    ),
                ),
            ],
            bases=("board.post",),
        ),
    ]
