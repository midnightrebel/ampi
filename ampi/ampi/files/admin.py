from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from ampi.ampi.files.models import File
from ampi.ampi.users.models import User


@admin.register(File)
class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'file')
    list_display = ('id', 'name', 'owner')
    list_display_links = ('id', 'name',)
    autocomplete_field = 'owner'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user.id
        super().save_model(request, obj, form, change)