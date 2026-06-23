from django.db import models
from django.utils import timezone
# Create your models here.
class Penvarity(models.Model):
    PEN_TYPE_CHOICE =[
        ('lg','linc-glyser'),
        ('bl','Ball-pen'),
        ('dm','Doms'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pens/')
    dtae_added = models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=PEN_TYPE_CHOICE)
    company=models.TextField(default='')


def __str__(self):
    return self.name


