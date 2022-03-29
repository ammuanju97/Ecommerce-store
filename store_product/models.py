from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class Product(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    price = models.IntegerField(default = 0)
    description = models.CharField(max_length = 200, default = '', null = True, blank = True)
    image = models.ImageField(upload_to='store_product/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else: 
            return Product.get_all_products()


