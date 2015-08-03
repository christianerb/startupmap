"""startupmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'^$', coreviews.LandingView.as_view()),
	url(r'startups/$', login_required(coreviews.StartupListView.as_view()), name='startup_list'),
	url(r'startup-map/$', login_required(coreviews.StartupMapView.as_view()), name='startup_map'),	
	url(r'startups/(?P<pk>\d+)/detail/$', login_required(coreviews.StartupDetailView.as_view()), name='startup_detail'),
	url(r'search/$', coreviews.SearchListView.as_view()),
    url(r'admin/', include(admin.site.urls)),
    url(r'startups/add/$', login_required(coreviews.StartupCreateView.as_view()), name='startup_add'),
    url(r'startups/(?P<pk>\d+)/delete/$', login_required(coreviews.StartupDeleteView.as_view()), name='startup_delete'),
    url(r'startups/(?P<pk>\d+)/update/$', login_required(coreviews.StartupUpdateView.as_view()), name='startup_update'),
    url(r'entrance/$', coreviews.entrance, name='signin_page'),  
    url(r'logout/$', coreviews.logout_view, name='logged_out'), 
    url(r'filtered/$', coreviews.index_filtered, name='list_filtered'),

)
