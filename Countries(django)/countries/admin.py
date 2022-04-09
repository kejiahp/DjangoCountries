from django.contrib import admin

# Register your models here.
from countries.models import Country2

class Country2Admin(admin.ModelAdmin):
    list_display = ('id','name','cioc','callingCodes')
    list_display_links = ('id','name')
    list_filter = ('region',)
    search_fields = ('name',)

admin.site.register(Country2,Country2Admin)

admin.site.site_header = 'Countries Administration Page'
