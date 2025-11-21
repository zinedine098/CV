from django.db import models

# Create your models here.
class tutor(models.Model):
    nama_tutor = models.CharField(max_length=200)
    keahlian = models.ForeignKey('course.kategori', on_delete=models.CASCADE)
    pengalaman = models.TextField()
    kontak = models.CharField(max_length=200)
    email = models.EmailField()
    nomor_telepon = models.CharField(max_length=15)
    alamat = models.TextField()

    def __str__(self):
        return self.nama_tutor

class aboutTutor(models.Model):
    tentang = models.TextField()

class experienceTutor(models.Model):
    tahun = models.CharField(max_length=4)
    judul = models.CharField(max_length=200)
    sub_judul = models.CharField(max_length=200)
    deskripsi = models.TextField()

    def __str__(self):
        return self.judul

class courseTutor(models.Model):
    tutor = models.ForeignKey('tutor', on_delete=models.CASCADE)
    course = models.ForeignKey('course.course', on_delete=models.CASCADE)

    def __str__(self):
        return f"Detail for {self.tutor.nama_tutor}"