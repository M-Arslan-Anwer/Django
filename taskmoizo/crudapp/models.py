from django.db import models

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=35)
    email = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=20)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.name, self.email, self.phoneNum, self.language, self.currency)

class Polygon(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.provider, self.name, self.price, self.latitude, self.longitude)


