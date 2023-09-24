from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class AuthorAdmin(admin.ModelAdmin):
    pass
