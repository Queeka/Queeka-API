from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .models.order_models import Shipment, ShipmentStatus, Package


admin.site.site_header = 'Queeka'
admin.site.site_title = 'Queeka Super Admin'


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('contact', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('contact',)
    ordering = ('contact',)

    fieldsets = (
        (None, {'fields': ('contact', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('contact', 'password1', 'password2'),
        }),
    )


class ShipmentDisplay(admin.ModelAdmin):
    list_display = ["shipment_sn", "tracking_id", "type",  "delivery_service", "created_at", "updated_at"]
    list_select_related = ["delivery_service"]
    list_per_page = 10
    
    ordering = ['-created_at']



admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Shipment, ShipmentDisplay)
admin.site.register(ShipmentStatus)
admin.site.register(Package)