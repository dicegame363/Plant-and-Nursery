from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator

class Nursery(models.Model):
    owner = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="nursery")

    def __str__(self):
        return f"{self.owner.name}"

class Plant(models.Model):
    nursery = models.ForeignKey(Nursery,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

class Order(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="orders")

class OrderProperty(models.Model):
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="plants")
    quantity = models.PositiveIntegerField()