from django.contrib import admin
from .models import User, Country

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Country)
