from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    reporting_period = models.CharField(max_length=50)

class BusinessUnit(models.Model):
    company = models.ForeignKey(Company, related_name='business_units', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Metric(models.Model):
    CATEGORY_CHOICES = [
        ('environmental', 'Environmental'),
        ('social', 'Social'),
        ('governance', 'Governance'),
    ]
    business_unit = models.ForeignKey(BusinessUnit, related_name='metrics', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    value = models.FloatField()
    year = models.PositiveIntegerField()
