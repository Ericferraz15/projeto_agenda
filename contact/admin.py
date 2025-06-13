from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','fist_name', 'last_name', 'fone', 'email', 'created_date',)
    ordering = ("id",)

    search_fields = ("id", "fist_name", "last_name", )
    list_per_page = 10
    list_max_show_all = 1000
    list_editable = ('fist_name', 'last_name', 'fone', 'email',)
    list_display_links = ('id', ) 