# Generated by Django 5.0.6 on 2024-05-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_customuser_managers_alter_customuser_is_admin_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]