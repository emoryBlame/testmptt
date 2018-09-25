from django.urls import path, include, re_path
from . import views

app_name = 'api'

urlpatterns = [
    re_path(r'page=(?P<page>[0-9]+)/$', views.home),
    re_path(r'group=(?P<groupname>[a-zA-Z0-9 ]*)/$', views.get_group),
    path('addElem/', views.addElem),
    path('', views.home),
]