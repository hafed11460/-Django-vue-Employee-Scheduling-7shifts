from restaurant.models import Location, Restaurant
from django.contrib import admin

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', )


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name','restaurant','id', )



admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Location,LocationAdmin)
