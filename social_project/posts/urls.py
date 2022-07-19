from django.urls import path,re_path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostListView.as_view(),name='all'),
    path('create/',views.PostCreateView.as_view(),name='create'),
    path(r'by/(?P<username>[-\w]+)/',views.UserPostsListView.as_view(),name='for_user'),
    path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='single'),
    path(r'delete/(?P<pk>\d+)/$',views.PostDeleteView.as_view(),name='delete'),
]
