from django.db import models


# Create your models here.

class Product(models.Model):
    class RatingChoice(models.IntegerChoices):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    rating = models.IntegerField(choices=RatingChoice.choices, default=RatingChoice.Zero.value)
    amount = models.IntegerField(default=1)
    discount = models.IntegerField()

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE, related_name='images')



class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)


class ProductAttribute(models.Model):
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('app.Attribute', on_delete=models.CASCADE)

class Customers(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email= models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)
    Joined = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.name}'