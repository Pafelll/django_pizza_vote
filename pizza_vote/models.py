from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=25)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Vote(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pizza}: {self.votes}'
