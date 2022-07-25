from django.db import models
from django.contrib.auth.models import User

# Create your models here.


INSTITUTIONS = [
    ('fundacja', 'fundacja'),
    ('organizacja pozarządowa', 'organizacja pozarządowa'),
    ('zbiórka lokalna', 'zbiórka lokalna')
    ]




class Category(models.Model):
    name = models.CharField(max_length=96)
    def __str__(self):
        return self.name




class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(choices=INSTITUTIONS, max_length=30, default="fundacja")
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name



