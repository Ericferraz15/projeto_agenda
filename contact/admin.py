from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone', 'email', 'created_date',)
    ordering = ("id",)

    search_fields = ("id", "first_name", "last_name", )
    list_per_page = 10
    list_max_show_all = 1000
    list_editable = ('first_name', 'last_name', 'phone', 'email',)
    list_display_links = ('id', ) 

@admin.register(models.category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ("id",)

