from django.db import models

class Games(models.Model):
    Rank = models.IntegerField()
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

class contact(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=400)

    def __str__(self):
        return self.email + ' ' +self.message

