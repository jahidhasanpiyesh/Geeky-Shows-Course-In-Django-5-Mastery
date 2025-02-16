from django.contrib import admin
from home.models import home, homeapp

# Register your models here.
class homeadmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'city']

admin.site.register(home, homeadmin)

@admin.register(homeapp)
class homeappadmin(admin.ModelAdmin):
    list_display = ['name', 'location']