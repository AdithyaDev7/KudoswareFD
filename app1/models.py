from django.db import models

# Create your models here.
# Here the class name represents the Table name in the Database and the attributes represents the column name
class Details(models.Model):
    Name=models.CharField(max_length=50)
    DOB=models.CharField(max_length=10)
    Gender=models.CharField(choices=(('M','Male'),('F','Female')),max_length=20)
    Email=models.EmailField(max_length=50)
    Work_Experience=models.IntegerField()
    Resume=models.FileField(upload_to='resumes/')