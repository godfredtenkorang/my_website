from django.contrib import admin
from .models import *


# admin.site.register(Contact)
# admin.site.register(Category)
# admin.site.register(Portfolio)

class PortfolioInLine(admin.TabularInline):
    model = Portfolio
    extra = 3
    
  
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name']})]
    inlines = [PortfolioInLine]
  
  
admin.site.register(Category, CategoryAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']
    
