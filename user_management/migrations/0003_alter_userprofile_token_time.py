# Generated by Django 3.2.15 on 2023-05-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_management", "0002_alter_userprofile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="token_time",
            field=models.DateTimeField(null=True),
        ),
    ]