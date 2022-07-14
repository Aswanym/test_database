from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=100,null=True)
    app_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title


class SecondProduct(models.Model):
    fist_title = models.ForeignKey('Product', on_delete=models.CASCADE)
    second_title = models.CharField(max_length=100,null=True)
    second_content = models.CharField(max_length=100,null=True)
    second_app_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.second_title