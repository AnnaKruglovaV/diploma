from django.db import models


class Home(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название темы",
        help_text="Введите название темы",
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото темы",
    )
    description = models.TextField(
        verbose_name="Описание темы",
        help_text="Введите описание темы",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        blank=True, null=True, verbose_name="Цена", help_text="Укажите цену за покупку"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        null=True,
        blank=True,
        related_name="categories",
    )
    restrictions = models.TextField(
        verbose_name="Ограничения",
        help_text="Укажите любые ограничения на продукт",
        blank=True,
        null=True,
    )
    medical_indications = models.TextField(
        verbose_name="Медицинские показания",
        help_text="Укажите медицинские показания",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name
