from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Hotel)
class HotelAmdin(admin.ModelAdmin):
    list_display=["id","name","hotel_type",]


# @admin.site.register(models.HotelImage)


# @admin.register(Hotel)
# class HotelAmdin(admin.ModelAdmin):
#     list_display=["id","name","hotel_type"]