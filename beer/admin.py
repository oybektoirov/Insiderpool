from django.contrib import admin
from beer.models import Beer, Brewery

class BeerAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'brewery', 'locality', 'description')
	search_fields = ['name']

class BreweryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'description')
	search_fields = ['name']

admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery, BreweryAdmin)


