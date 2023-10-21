from django.db import models

# Create your models here.
class sites(models.Model):
  name = models.CharField(max_length=250, verbose_name='Sites Name')
  address = models.CharField(max_length=250, verbose_name='Address')
  lat = models.FloatField(verbose_name='Latitude')
  long = models.FloatField(verbose_name='Length')

  class Meta:
    verbose_name = 'Site'
    verbose_name_plural = 'Sites'
    ordering = ['name']

    def __str__(self):
      return self.name