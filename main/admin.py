from django.contrib import admin

# Register your models here.
from .models import Location, Comment

admin.site.register(Location)
admin.site.register(Comment)