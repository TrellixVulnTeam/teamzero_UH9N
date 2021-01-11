from django.db import models

class Games(models.Model):
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=60)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    NA_Sales = models.IntegerField()
    EU_Sales = models.IntegerField()
    JP_Sales = models.IntegerField()
    Other_Sales = models.IntegerField()
    Global_Sales = models.IntegerField()

