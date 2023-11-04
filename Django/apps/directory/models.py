from django.db import models

# Create your models here.
class Friend(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
      text = "[{0}] {1}"
      return text.format(text, self.fullname)