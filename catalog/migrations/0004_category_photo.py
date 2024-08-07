# Generated by Django 5.0.7 on 2024-08-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_product_medical_indications_product_restrictions"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото категории",
                null=True,
                upload_to="product/photo",
                verbose_name="Изображение",
            ),
        ),
    ]
