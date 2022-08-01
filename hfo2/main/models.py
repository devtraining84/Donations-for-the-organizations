
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


INSTITUTIONS = [
    ('fundation', 'fundacja'),
    ('non_gov', 'organizacja pozarządowa'),
    ('local', 'zbiórka lokalna')
    ]




class CategoryModel(models.Model):
    name = models.CharField(max_length=96)
    def __str__(self):
        return f"{self.id} : {self.name}"



class InstitutionModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(choices=INSTITUTIONS, max_length=30, default="fundacja")
    categories = models.ManyToManyField(CategoryModel)
    
    def __str__(self):  
        stringtoreturn = f"nazwa: {self.name} typ: {self.type} categoria:{self.categories} opis:{self.description}"
        return stringtoreturn



# class Donation(models.Model):
#     quantity = models.PositiveSmallIntegerField()
#     categories = models.ManyToManyField(Category)
#     institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
#     address = models.CharField(max_length=40)
#     phone_number = models.PositiveIntegerField()
#     city = models.CharField(max_length=32)
#     zip_code = models.CharField(max_length=6)
#     pick_up_date = models.DateField()
#     pick_up_time = models.DateTimeField()
#     pick_up_comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="Null")
    
#     def __str__(self):
#         return self.id


