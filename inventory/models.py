from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "📕 Тип"


class Price(models.Model):
    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.amount} {self.currency}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "📮 Цена (Price)"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    barcode = models.CharField(max_length=100, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def reduce_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Количество для уменьшения должно быть положительным числом.")

        if self.quantity >= quantity:
            self.quantity -= quantity
            self.save()  # Сохраняем изменения в базе данных
        else:
            raise ValueError("Недостаточно товара на складе для уменьшения.")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "🧮 Продукт"