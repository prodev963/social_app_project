from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic

from .models import Group,GroupMember
# Create your views here.

class GroupCreateView(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description')
    model = Group

class GruopDetailView(generic.DetailView):
    model= Group

class GroupsListView(generic.ListView):
    model = Group
    
            
