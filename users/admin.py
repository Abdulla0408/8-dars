from django.contrib import admin
from .models import User, Team, Student


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Team)
