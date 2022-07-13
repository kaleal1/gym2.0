from django.contrib import admin
from .models import User, Routine
from .models import Excercise
# Register your models here.

admin.site.register(User)
admin.site.register(Excercise)
admin.site.register(Routine)

