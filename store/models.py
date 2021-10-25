from django.db import models


class Product(models.Model):
    name = models.CharField('наименование', max_length=100)
    price = models.DecimalField('цена', max_digits=15, decimal_places=2)
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField('наименование', max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'категория товаров'
        verbose_name_plural = 'категории товаров'

    def __str__(self) -> str:
        return self.name
