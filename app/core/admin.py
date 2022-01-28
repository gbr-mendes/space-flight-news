from django.db.models.functions import Greatest
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Persmissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': 'wide',
            'fields': ('email', 'password1', 'password2')
        }),
    )

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Launch)
admin.site.register(models.Event)
