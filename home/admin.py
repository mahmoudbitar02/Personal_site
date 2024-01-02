from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Home)
admin.site.register(models.About)
admin.site.register(models.Service)
admin.site.register(models.Portfoilo)
admin.site.register(models.Blog)
admin.site.register(models.Cattigory)
admin.site.register(models.Skill)