from django.db import models


class Category(models.Model):
    name = models.CharField()
    is_active = models.BooleanField(default=True)


class Dishes(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Tables(models.Model):
    status = models.CharField()
    is_active = models.BooleanField(default=True)





class Orders(models.Model):
    user_name = models.CharField()
    dish = models.ManyToManyField(Dishes)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)