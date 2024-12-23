from django.db import models

# Create your models here.
class Form (models.Model):
  fname = models.CharField(max_length = 100)
  lname = models.CharField(max_length = 100)
  company = models.CharField(max_length = 100, blank = True, null = True)
  email = models.EmailField(max_length = 100)
  phone = models.BigIntegerField(max_length = 10)
  sub = models.CharField(max_length = 100)
  message = models.CharField(max_length = 400)
  published_date = models.DateTimeField(auto_now_add = True)
  def __str__(self):
    return self.fname