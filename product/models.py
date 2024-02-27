from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField("Активна", default=False)
    # ForeignKey
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Родитель")

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    class StockStatus(models.TextChoices):
        IN_STOCK = 'IS', 'In Stock'
        OUT_OF_STOCK = 'OOS', 'Out of stock'
        BACKORDERED = 'BO', 'Back Ordered'

    pid = models.CharField("Идентификатор", max_length=255, null=False, blank=False, unique=True)
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField("Описание", blank=True, null=True)
    is_digital = models.BooleanField("Цифровые данные", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, editable=False)
    is_active = models.BooleanField("Наличие", default=True)
    stock_status = models.CharField("Статус товара", max_length=3, choices=StockStatus.choices,
                                    default=StockStatus.OUT_OF_STOCK)
    stock_qty = models.IntegerField("Кол-во на складе", default=0)
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    # ForeignKey
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")

    # ManyToMany
    product_type = models.ManyToManyField('ProductType', related_name='product_type',
                                          verbose_name="Тип продукта")
    attribute_values = models.ManyToManyField('AttributeValue', related_name='attribute_values',
                                              verbose_name='Значение атрибута')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField("Фото")
    # ForeignKey
    product_line = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Линейка продуктов")


class Attribute(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True, null=True)
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE, verbose_name="Тип продукта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Атрибуты"


class AttributeValue(models.Model):
    attribute_value = models.CharField(" Значение атрибута", max_length=100)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, verbose_name="Атрибут")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")

    def __str__(self):
        return f"{self.attribute}:{self.attribute_value}"


class ProductType(models.Model):
    name = models.CharField("Название", max_length=100)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name="Родитель", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Тип продукта"

