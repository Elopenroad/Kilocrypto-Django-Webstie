from django.contrib import admin
from .models import Service



class ServiceeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Service, ServiceeAdmin)