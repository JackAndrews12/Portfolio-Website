from django.contrib import admin
from .models import Project, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'linkedin')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
