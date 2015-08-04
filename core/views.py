from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from sitegate.decorators import redirect_signedin, sitegate_view, signup_view
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import core.models as coremodels

# Create your views here.
class LandingView(TemplateView):
	template_name = "base/index.html"

	def get_context_data(self, **kwargs):
		context = super(LandingView, self).get_context_data(**kwargs)
		latest_all = coremodels.Startup.objects.all().order_by('created_on')
		latest_startup = coremodels.Startup.objects.all().order_by('created_on')
		context['last_ones'] = latest_all.reverse()[:2]
		context['latest_startup'] = latest_startup[:5]
		return context

class StartupListView(ListView):
	model = coremodels.Startup
	template_name= "startups/list.html"

class SearchListView(StartupListView):
	
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.Startup.objects.filter(title__icontains=incoming_query_string)

class StartupMapView(ListView):
	model = coremodels.Startup
	template_name= "startups/map.html"

class StartupCreateView(CreateView):
	model = coremodels.Startup
	template_name = "base/form.html"
	fields = "__all__"


class StartupDeleteView(DeleteView):
	model = coremodels.Startup
	template_name = "base/confirmation.html"
	fields = "__all__"	
	success_url = reverse_lazy(viewname="startup_list")

class StartupUpdateView(UpdateView):
	model = coremodels.Startup
	template_name = "base/form.html"
	fields = "__all__"

class StartupDetailView(DetailView):
	model = coremodels.Startup
	template_name = "startups/detail.html"
	context_object_name = "startup"

	def get_context_data(self, **kwargs):
		context = super(StartupDetailView, self).get_context_data(**kwargs)
		startup = coremodels.Startup.objects.get(id=self.kwargs['pk'])
		return context

@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.ign up page.
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})

def logout_view(request):
  auth.logout(request)
  # Redirect to a success page.
  return render(request, "base/index.html")
