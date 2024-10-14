from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    data = models.DateField(default=True)

    def __str__(self):
        return self.fio
    

class Tariffs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    

class Areas(models.Model):
    id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.place
    

class Records(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(max_length=100)

    def __str__(self):
        return self.time
    

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.price
