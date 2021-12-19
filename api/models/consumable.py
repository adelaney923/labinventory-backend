from django.db import models
from django.contrib.auth import get_user_model

class Consumable(models.Model):
  description = models.CharField(max_length=100)
  storage_temp = models.CharField(max_length=100)
  reference_num = models.CharField(max_length=100)
  part_number = models.CharField(max_length=100)
  unit_of_measure = models.CharField(max_length=100)
  quantity = models.IntegerField()
  lot_number = models.IntegerField()
  expiration_date = models.CharField(max_length=100)
  comments = models.CharField(max_length=500, blank=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    # This must return a string
    return f"{self.description} expires on {self.expiration_date}"