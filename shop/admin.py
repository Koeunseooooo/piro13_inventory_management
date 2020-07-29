from django.contrib import admin
from .models import Account



@admin.register(Account)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','Name', 'Call', 'Address']
    list_display_links = ['Name']
    search_fields =  ['Name']