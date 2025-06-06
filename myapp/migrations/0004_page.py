# Generated by Django 5.1.5 on 2025-02-04 18:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_news_mini_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
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
                        blank=True, default="", max_length=255, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Слаг"),
                ),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Страница",
                "verbose_name_plural": "Страницы",
                "ordering": ["-created_at"],
            },
        ),
    ]
