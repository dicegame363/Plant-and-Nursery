from django.contrib import admin

# Register your models here.
from .models import Plant,Order,Nursery

admin.site.register(Plant)
admin.site.register(Order)
admin.site.register(Nursery)