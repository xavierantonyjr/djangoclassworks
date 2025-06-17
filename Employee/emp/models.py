from django.db import models

# Create a model named Employee with fields (name,age,salary,designation,place,image,department_name)
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    designation = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employee')
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
