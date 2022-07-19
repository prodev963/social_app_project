from django.urls import path,re_path
from . import views

app_name="groups"

urlpatterns = [
    path("",views.GroupsListView.as_view(),name='all'),
    path("new/",views.GroupCreateView.as_view(),name='create'),
    path(r"posts/in/(?P<slug>[-\w]+)/$",views.GruopDetailView.as_view(),name='single'),
    
]
