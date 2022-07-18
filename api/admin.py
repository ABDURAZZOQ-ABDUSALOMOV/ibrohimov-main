from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Shop)
admin.site.register(Product)

admin.site.register(Currency)
admin.site.register(Types)



