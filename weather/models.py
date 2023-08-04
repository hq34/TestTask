from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class TemperatureRecord(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    temperature_c = models.FloatField()

    class Meta:
        unique_together = ('city', 'date')

    def __str__(self):
        return self.city, self.date, self.temperature_c
