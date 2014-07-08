from django.contrib import admin	
from school.models import School

class SchoolAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'school_type', 'city', 'state')
	search_fields = ['name']
	
admin.site.register(School, SchoolAdmin)
