from django.contrib import admin

from ampi.ampi.reports.models import Report


@admin.register(Report)
class UserAdmin(admin.ModelAdmin):
    fields = ('id_file', 'count_down')
    list_display = ('id', 'id_file', 'count_down')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.id_file = request.user.id
        super().save_model(request, obj, form, change)
