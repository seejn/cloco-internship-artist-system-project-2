# Generated by Django 5.0.6 on 2024-05-21 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_artistdetails_table"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ArtistDetails",
            new_name="ArtistDetail",
        ),
    ]
