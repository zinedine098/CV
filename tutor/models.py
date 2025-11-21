from django.db import models

# Create your models here.
class tutor(models.Model):
    nama_tutor = models.CharField(max_length=200)
    keahlian = models.CharField(max_length=200)
    pengalaman = models.TextField()

    def __str__(self):
        return self.nama_tutor