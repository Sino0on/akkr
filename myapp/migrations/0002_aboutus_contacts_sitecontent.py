# Generated by Django 5.1.5 on 2025-02-04 12:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "image1",
                    models.FileField(
                        upload_to="images/", verbose_name="Первое изображение"
                    ),
                ),
                (
                    "image2",
                    models.FileField(
                        upload_to="images/", verbose_name="Второе изображение"
                    ),
                ),
                (
                    "image3",
                    models.FileField(
                        upload_to="images/", verbose_name="Третье изображение"
                    ),
                ),
                (
                    "title2",
                    models.CharField(max_length=255, verbose_name="Второе Название"),
                ),
                (
                    "description2",
                    ckeditor.fields.RichTextField(verbose_name="Второе Описание"),
                ),
                (
                    "image4",
                    models.FileField(
                        upload_to="images/", verbose_name="Четвертое изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "О нас",
                "verbose_name_plural": "О нас",
            },
        ),
        migrations.CreateModel(
            name="Contacts",
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
                    "address",
                    models.CharField(
                        blank=True, default="", max_length=255, verbose_name="Адрес"
                    ),
                ),
                (
                    "link_address",
                    models.TextField(
                        blank=True, default="", verbose_name="Ccылка на адрес"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        default="", max_length=123, verbose_name="Номер телефона"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        default="22116708", max_length=123, verbose_name="Почта"
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакты",
                "verbose_name_plural": "Контакты",
            },
        ),
        migrations.CreateModel(
            name="SiteContent",
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
                    "original_text",
                    models.TextField(
                        help_text="Оригинальный текст, который отображается на сайте.",
                        max_length=20000,
                        verbose_name="Оригинальный текст",
                    ),
                ),
                (
                    "current_text",
                    models.TextField(
                        help_text="Измененный или текущий текст, который отображается на сайте.",
                        max_length=20000,
                        verbose_name="Текущий текст",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контент сайта",
                "verbose_name_plural": "Контент сайта",
            },
        ),
    ]
