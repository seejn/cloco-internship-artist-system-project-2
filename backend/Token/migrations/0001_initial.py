# Generated by Django 5.0.6 on 2024-05-24 03:15

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
            name="Token",
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
                ("t_type", models.CharField(max_length=50, null=True, unique=True)),
                ("token", models.CharField(max_length=250, unique=True)),
                (
                    "expiry",
                    models.PositiveIntegerField(
                        default=1716605124,
                        validators=[
                            django.core.validators.MaxValueValidator(99999999999)
                        ],
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="token",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "tokens",
            },
        ),
    ]