from django.contrib import admin
from app import models

admin.site.register(models.Profile)
admin.site.register(models.Tag)
admin.site.register(models.Like)
admin.site.register(models.Question)
admin.site.register(models.Answer)


# Register your models here.
