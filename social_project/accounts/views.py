from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,ListView,CreateView,UpdateView,DeleteView,DetailView,TemplateView
from . import models,forms
# Create your views here.

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name: str = 'accounts/signup.html '