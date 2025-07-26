from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bookshelf.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('birth_date', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('birth_date', 'profile_photo')}),
    )

