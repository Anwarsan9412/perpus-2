from django.shortcuts import render
from  django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name= 'registration/user_profile.html'

    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(self, *args, **kwargs)
    #     context['heading'] = "Halaman Home"
    #     return context
