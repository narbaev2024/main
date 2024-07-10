from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name_product = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    active = models.BooleanField(default=True)
    phone_number = models.IntegerField(verbose_name='Тел номер')
    created_date = models.DateField()
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.name_product


class Comment(models.Model):
    user_name = models.CharField(max_length=32)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.user_name} - {self.product}'