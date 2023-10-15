from django.db import models

# Create your models here.
class Contact(models.Model):
  date = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=90)
  last_name = models.CharField(max_length=90)
  email = models.EmailField(max_length=90)
  phone = models.CharField(max_length=10)
  message = models.CharField(max_length=2000)


  def __str__(self):
    text = "[{0}] {1}"
    return text.format(text, self.name)