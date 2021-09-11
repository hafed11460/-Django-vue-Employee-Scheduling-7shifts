from employee.models import Employee, EmployeeProfileImage, Role
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class EmployeeAdmin(UserAdmin):
    list_display = ('email','location','id', 'first_name', 'last_name','date_joined', 'last_login', 'is_admin', 'is_staff','is_active', )
    search_fields = ('email',)
    readonly_fields = ('id', 'date_joined', 'last_login', )
    ordering= ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'password1', 'password2','location'),
        }),
    )



class RoleAdmin(admin.ModelAdmin):
    list_display= ['name', 'id']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeProfileImage)

admin.site.register(Role,RoleAdmin)
