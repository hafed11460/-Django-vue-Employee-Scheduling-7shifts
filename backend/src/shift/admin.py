from shift.models import Shift
from django.contrib import admin



class ShiftAdmin(admin.ModelAdmin):
    list_display = ('location','starthour', 'endhour', 'employee','date','id', )

admin.site.register(Shift,ShiftAdmin)
