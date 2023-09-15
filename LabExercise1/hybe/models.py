from django.db import models

# Create your models here.
# Create your models here.
class Artist(models.Model):  
    img = models.FileField()
    birthname = models.CharField(max_length=100)  
    stagename = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.IntegerField()
    
   
    class Meta:  
        db_table = "tblartists"