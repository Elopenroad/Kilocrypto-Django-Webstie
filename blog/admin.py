from django.contrib import admin

from .models import Blog

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Blog, ArticleAdmin)