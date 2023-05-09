# Generated by Django 4.2 on 2023-05-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                    "title",
                    models.CharField(
                        choices=[
                            ("E", "오류"),
                            ("U", "불편사항"),
                            ("R", "건의사항"),
                            ("C", "칭찬"),
                        ],
                        max_length=10,
                    ),
                ),
                ("content", models.CharField(max_length=255)),
                ("is_checked", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
