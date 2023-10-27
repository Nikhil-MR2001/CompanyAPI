from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    about = models.TextField(null=True, blank=True, default="company description goes here....")
    type = models.CharField(max_length=100, choices=(
                ('IT' , 'IT'),
                ('Non IT', 'Non IT'),
            ))
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    emain = models.EmailField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone_number = models.PositiveIntegerField()
    about = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=100,choices=(
                    ('Manager', 'Manager'),
                    ('Developer', 'Developer'),
                    ('HR Manager', 'HR Manager'),
                ))


    def __str__(self):
        return self.name