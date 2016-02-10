from __future__ import unicode_literals
from django.template.defaultfilters import slugify
import uuid

from django.db import models

class Bares(models.Model):
    nombre= models.CharField(max_length=128, unique=True)
    direccion=models.CharField(max_length=180)
    visitas = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Bares, self).save(*args, **kwargs)
    
    def __unicode__(self):
		return self.nombre
        
class Tapas(models.Model):
    nombrebar = models.ForeignKey(Bares)
    nombre = models.CharField(max_length=120)
    votos = models.IntegerField(default=0)
    
    def __unicode__(self):
		return self.nombre