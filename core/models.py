from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from geoposition.fields import GeopositionField

# Create your models here.
class Startup(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(max_length=1000, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	location = GeopositionField(null=True, blank=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname="startup_list")