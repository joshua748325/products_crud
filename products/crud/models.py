from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=256)
    sold=models.IntegerField()
    total=models.IntegerField()
    price=models.FloatField()
    review=models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.review} star, {self.price} rupees."