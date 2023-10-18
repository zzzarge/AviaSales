from django.contrib import admin

from .models import Comment, Country, CityImages, City, PopularPlaces, LocalPlaces, Ticket, UserTicket




admin.site.register(Comment)
admin.site.register(Country)
admin.site.register(CityImages)
admin.site.register(City)
admin.site.register(PopularPlaces)
admin.site.register(LocalPlaces)
admin.site.register(Ticket)
admin.site.register(UserTicket)