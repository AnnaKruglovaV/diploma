# Generated by Django 5.0.7 on 2024-08-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_category_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Home",
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
                    "name",
                    models.CharField(
                        help_text="Введите название темы",
                        max_length=150,
                        verbose_name="Название темы",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото темы",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Изображение",
                    ),
                ),
            ],
        ),
    ]
