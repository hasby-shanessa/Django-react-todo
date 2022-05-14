from django.contrib import admin
from .models import Todo

#username: moi----------------email:umutonihasby@gmail.com------------------psswrd:Umutonihasby@123

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'completed')

admin.site.register(Todo, TodoAdmin)
