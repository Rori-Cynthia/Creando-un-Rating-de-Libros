from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AccountUser, Book

admin.site.site_header = 'Curso Django' 
admin.site.index_title = 'Panel de control Proyecto Django' 
admin.site.site_title = 'Administrador Django'

@admin.register(AccountUser)
class CustomUserAdmin(UserAdmin):
    model = AccountUser
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'valuation', 'get_rating')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('valuation', 'updated_at')

    def get_rating(self, obj):
        if obj.valuation < 1000:
            return 'Baja'
        elif 1000 <= obj.valuation <= 2500:
            return 'Media'
        else:
            return 'Alta'
    
    get_rating.short_description = 'Rating'
