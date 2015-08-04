from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from geoposition.fields import GeopositionField

CATEGORY_CHOICES = (
	(0, "Startup"),
	(1, "Investor"),
	(2, "Other"),
	(3, "Accelerator"),
	(4, "Incubator"),
	)
	

# Create your models here.
class Startup(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(max_length=1000, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	location = GeopositionField(null=True, blank=True)
	category = models.IntegerField(choices=CATEGORY_CHOICES, null=True)
	created_on = models.DateTimeField(auto_now_add=True, editable=False)
	submitter = models.ForeignKey(User)


	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname="startup_list")

class Vote(models.Model):
	voter = models.ForeignKey(User)
	startup = models.ForeignKey(Startup)

	def __unicode__(self):
		return "%s upvoted %s" % (self.voter.username, self.startup.title)

