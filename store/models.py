from django.db import models

class Games(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=60)
    year = models.IntegerField(default=None)
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    NA_Sales = models.IntegerField(default=None)
    EU_Sales = models.IntegerField(default=None)
    JP_Sales = models.IntegerField(default=None)
    Other_Sales = models.IntegerField(default=None)
    Global_Sales = models.IntegerField(default=None)

    def __str__(self):
        return self.Name
class contact(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=400)

    def __str__(self):
        return self.email + ' ' +self.message

