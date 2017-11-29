from django.db import models

# Create your models here.
class Birthdays(models.Model):
    name = models.CharField(max_length=30)
    bthday_date = models.DateField()


