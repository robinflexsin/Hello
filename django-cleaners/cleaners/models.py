from django.db import models

class Cities(models.Model):
    name = models.CharField(max_length=100
)
    def __str__(self):
        return self.name

class Cleaner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.ForeignKey(Cities)
    quality_score = models.DecimalField(max_digits=5, decimal_places=2)