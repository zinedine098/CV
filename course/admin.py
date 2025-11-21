from django.contrib import admin
# import semua table di models.py
from .models import kategori, level, durasi, is_paid, course

# Register your models here.
admin.site.register(kategori)
admin.site.register(level)
admin.site.register(durasi)
admin.site.register(is_paid)
admin.site.register(course)
