from django.db import models

class Games(models.Model):
    Rank = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Platform = models.CharField(max_length=60)
    Year = models.IntegerField()
    Genre = models.CharField(max_length=50)
    Publisher = models.CharField(max_length=50)
    NA_Sales = models.IntegerField()
    EU_Sales = models.IntegerField()
    JP_Sales = models.IntegerField()
    Other_Sales = models.IntegerField()
    Global_Sales = models.IntegerField()


