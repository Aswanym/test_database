from django.db import models

# Create your models here.


class Order(models.Model):
    title = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=100,null=True)
    app_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = u'"order\".\"order"'


class SecondOrder(models.Model):
    fist_title = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    second_title = models.CharField(max_length=100,null=True)
    second_content = models.CharField(max_length=100,null=True)
    second_app_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.second_title

    class Meta:
        db_table = u'"order\".\"second_order"'

class NewOrder(models.Model):
    fist_title = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    second_title = models.CharField(max_length=100,null=True)
    second_content = models.CharField(max_length=100,null=True)
    second_app_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.second_title

    class Meta:
        db_table = u'"order\".\"new_order"'
