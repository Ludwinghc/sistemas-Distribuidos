from django.db import models

# Create your models here.
class Proyecto(models.Model):
  codigo = models.CharField(primary_key=True,max_length=4, null=False)
  nombre = models.CharField(max_length=90, null=False)
  descripcion = models.CharField(max_length=2000, null=False)
  date = models.DateField( auto_now=True, null=False)
  photo = models.ImageField(upload_to='media/photoProjects', null=True)
  publish = models.BooleanField(default=True)


  def __str__(self):
    texto = "[{0}] {1}"
    if self.publish:
      t_publish = "ON"
    else:
      t_publish = "OFF"
    return texto.format(t_publish, self.nombre)