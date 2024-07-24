from django.db import models

class Consultant(models.Model):
    name = models.CharField(max_length=255 , default="none")
    mail = models.EmailField(max_length=255 , default="none")

    def __str__(self):
        return self.name
