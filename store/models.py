from django.db import models

class Games(models.Model):
    ID = models.CharField(max_length=50,primary_key=True),
    Name = models.CharField(max_length=100),
    Platform = models.CharField(max_length=50),
    Year = models.IntegerField(),
    Genre = models.CharField(max_length=60),
    Publisher = models.CharField(max_length=30),
    NA_Sales = models.IntegerField(),
    EU_Sales = models.IntegerField(),
    JP_Sales = models.IntegerField(),
    Other_Sales = models.IntegerField(),
    Global_Sales = models.IntegerField(),

    def __str__(self):
        return self.Name


