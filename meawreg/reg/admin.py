from django.contrib import admin

from .models import Subject, Student, Apply
# Register your models here.

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Apply)
