from django.db import models
from django.contrib.localflavor.us.models import USStateField
from django.contrib.localflavor.us.us_states import US_STATES

SCHOOL_CHOICES = (
	('S', 'School'),
	('C', 'College'),
	('U', 'University'),
	('I', 'Institute'),
)

class School(models.Model):
	name = models.CharField(max_length=200)
	school_type = models.CharField(max_length=1, choices=SCHOOL_CHOICES)
	slug = models.SlugField(unique=True)
	address_1 = models.CharField(max_length=200)
	address_2 = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200)
	state = USStateField(choices=US_STATES)
	zipcode = models.CharField(max_length=30)
	description = models.TextField(blank=True)
	logo = models.ImageField(upload_to='images/schoollogo/', blank=True)
	
	def __unicode__(self):
		return self.name
	

