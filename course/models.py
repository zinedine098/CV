from django.db import models
from tutor.models import tutor

# Create your models here.

#filter course
class kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori

class level(models.Model):
    nama_level = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_level

class durasi(models.Model):
    nama_durasi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_durasi

class is_paid(models.Model):
    nama_price = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_price
    
class course(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='course_images/')
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    level = models.ForeignKey(level, on_delete=models.CASCADE)
    durasi = models.ForeignKey(durasi, on_delete=models.CASCADE)
    is_bayar = models.ForeignKey(is_paid, on_delete=models.CASCADE)
    tutor = models.ForeignKey(tutor, on_delete=models.CASCADE)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_diperbarui = models.DateTimeField(auto_now=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.judul