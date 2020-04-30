from django.db import models

# Create your models here.
class Destin(models.Model):

    name = models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    special= models.BooleanField(default=False)

    def __str__(self):
        return self.name