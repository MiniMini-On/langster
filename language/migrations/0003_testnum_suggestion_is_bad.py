# Generated by Django 4.2 on 2023-05-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("language", "0002_suggestion_is_checked_suggestion_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestNum",
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
                ("number", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="suggestion",
            name="is_bad",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]