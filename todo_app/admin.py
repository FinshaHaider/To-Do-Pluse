from django.contrib import admin
from .models import Tasks,Todo,Users,Notes
# Register your models here.



admin.site.register(Tasks)
admin.site.register(Todo)
admin.site.register(Users)
admin.site.register(Notes)


