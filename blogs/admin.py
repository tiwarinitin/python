from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Post._meta.fields]
    list_editable = ['content']

admin.site.register(Post, PostAdmin)