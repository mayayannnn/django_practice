from django.db import models

# Create your models here.

class Todo(models.Model):
    memo = models.CharField("memo",max_length=225)

    def __str__(self):
        return self.memo