
from re import T
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


INSTITUTIONS = [
    ('fundation', 'fundacja'),
    ('non_gov', 'organizacja pozarządowa'),
    ('local', 'zbiórka lokalna')
    ]




class CategoryModel(models.Model):
    
    class Meta:
        ordering = ('pk',)
    name = models.CharField(max_length=96)
        
    def __str__(self):
        return f"{self.id} : {self.name}"



class InstitutionModel(models.Model):
    class Meta:
        ordering = ('pk',)
        
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(choices=INSTITUTIONS, max_length=30, default="fundacja")
    categories = models.ManyToManyField(CategoryModel)
    
    def __str__(self):  
        stringtoreturn = f"nazwa: {self.name} typ: {self.type} categoria:{self.categories} opis:{self.description}"
        return stringtoreturn



class DonationModel(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(CategoryModel)
    institution = models.ForeignKey(InstitutionModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone_number = models.PositiveIntegerField()
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id


   
class TestModel(models.Model):
    quantity = models.PositiveSmallIntegerField()
  


class TestModel2(models.Model):
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    zip_code = models.CharField(max_length=6,blank=True, null=True)
    
    pick_up_date = models.DateField(blank=True, null=True)
    pick_up_time = models.TimeField(blank=True, null=True)
    
    pick_up_comment = models.TextField(blank=True, null=True)




class TestModel3(models.Model):
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    zip_code = models.CharField(max_length=6,blank=True, null=True)
    pick_up_date = models.DateField(blank=True, null=True)
    pick_up_time = models.TimeField(blank=True, null=True)
    pick_up_comment = models.TextField(blank=True, null=True) 
    categories = models.ManyToManyField(CategoryModel)   
    institution = models.ForeignKey(InstitutionModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id



# class TestModel3(models.Model):
#     quantity = models.PositiveSmallIntegerField(null=True, blank=True)
#     categories = models.ManyToManyField(CategoryModel)
#     institution = models.ForeignKey(InstitutionModel, on_delete=models.CASCADE)
#     address = models.CharField(max_length=40, null=True, blank=True)
#     phone_number = models.PositiveIntegerField(null=True, blank=True)
#     city = models.CharField(max_length=32, null=True, blank=True)
#     zip_code = models.CharField(max_length=6, null=True, blank=True)
#     pick_up_date = models.DateField(null=True, blank=True)
#     pick_up_time = models.DateTimeField(null=True, blank=True)
#     pick_up_comment = models.TextField(null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.id




    

                
                



