# Generated by Django 5.1.5 on 2025-04-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0011_application"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="application",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки",
            },
        ),
        migrations.AlterModelOptions(
            name="morepage",
            options={
                "ordering": ["created_at"],
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
        migrations.AddField(
            model_name="pageimage",
            name="file_type",
            field=models.CharField(
                blank=True,
                choices=[("image", "image"), ("file", "file")],
                default="image",
                max_length=123,
            ),
        ),
    ]
