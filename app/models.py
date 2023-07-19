from django.db import models

# Create your models here.


class ProductModel(models.Model):
    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)




    class Meta:
        db_table='product'



