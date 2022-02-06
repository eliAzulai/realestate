from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ConactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25