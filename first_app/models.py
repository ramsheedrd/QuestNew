from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['name']

    def __str__(self):
        return self.name
        



