from django.contrib import admin
import core.models as coremodels
# Register your models here.

admin.site.register(coremodels.Startup)
admin.site.register(coremodels.Vote)