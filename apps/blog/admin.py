from django.contrib import admin

from .models import Post, Category, Tag, Contact


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
