from django.db import models
from django.urls import reverse
# Create your models here.

class Cup(models.Model):
  color = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  type = models.TextField(max_length=250)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.color
    
  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'cup_id': self.id})
