from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AccountUser, Book


@admin.register(AccountUser)
class CustomUserAdmin(UserAdmin):
    model = AccountUser
    fieldsets = UserAdmin.fieldsets


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'valuation', 'Rating')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('valuation', 'updated_at')

    def get_rating(self, obj):
        if obj.valoracion < 1000:
            return 'Baja'
        elif 1000 <= obj.valoracion <= 2500:
            return 'Media'
        else:
            return 'Alta'
    
    get_rating.short_description = 'Rating'
