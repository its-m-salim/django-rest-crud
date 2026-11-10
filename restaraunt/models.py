from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class Dishes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Tables(models.Model):
    TABLE_STATUS = [
        ("free", "Свободен"),
        ("busy", "Занят"),
    ]

    number = models.IntegerField(unique=True)
    status = models.CharField(max_length=10, choices=TABLE_STATUS, default="free")
    is_active = models.BooleanField(default=True)


class Orders(models.Model):
    ORDER_STATUS = [
        ("new", "Новый"),
        ("cooking", "Готовится"),
        ("served", "Подан"),
        ("paid", "Оплачен"),
    ]

    user_name = models.CharField(max_length=100)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
