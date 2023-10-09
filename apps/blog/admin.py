from django.contrib import admin

from .models import Comment, Country, CityImages, City


admin.site.register(Comment)
admin.site.register(Country)
admin.site.register(CityImages)
admin.site.register(City)