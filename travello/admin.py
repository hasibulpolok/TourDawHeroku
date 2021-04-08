from django.contrib import admin
from .models import Destination
from .models import Phone_Number
from .models import NewsLater
# Register your models here.
admin.site.register(Destination)

admin.site.register(Phone_Number)

admin.site.register(NewsLater)
