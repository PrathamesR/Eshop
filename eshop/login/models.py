from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

    itemName = models.CharField(max_length=100)
    itemCost = models.CharField(max_length=5)
    itemDesc = models.CharField(max_length=1000)
    itemRat = models.CharField(max_length=1)
    itemType = models.CharField(max_length=1)
    itemPic = models.CharField(max_length=200,
                               default="https://pbs.twimg.com/profile_images/507251035929190400/BDUL3Uzt_400x400.png")

    def __str__(self):
        return self.itemName + '-' + self.itemCost + '-' + self.itemRat + '-' + self.itemDesc


class Order(models.Model):

    order = models.CharField(max_length=1, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.order + '-' + str(self.user) + '-' + str(self.item)

