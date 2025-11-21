from django.contrib import admin
from .models import tutor, aboutTutor, experienceTutor, courseTutor

# Register your models here.
admin.site.register(tutor)
admin.site.register(aboutTutor)
admin.site.register(experienceTutor)
admin.site.register(courseTutor)
