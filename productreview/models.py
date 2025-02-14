from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.name} for {self.price}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    rating = models.IntegerField()

    def __str__(self):
        return f"Review from {self.author} on {self.product} with rating {self.rating}"
    
    
