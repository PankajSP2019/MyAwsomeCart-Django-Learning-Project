from django.db import models


# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    # To show the product in the list as the name of product name in Admin Panel
    def __str__(self):
        show_id_and_name = f"{self.id} - {self.product_name}"
        return show_id_and_name
        # return self.product_name
