from django.db import models

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

class price(models.Model):
    nama_price = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_price
    
class course(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    level = models.ForeignKey(level, on_delete=models.CASCADE)
    durasi = models.ForeignKey(durasi, on_delete=models.CASCADE)
    price = models.ForeignKey(price, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul