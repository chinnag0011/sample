"""movie_project URL Configuration

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
from django.conf.urls import patterns, include, url
#from django.contrib import admin
from django.contrib import admin
from MovieLib import views
from MovieLib.views import *

from django.contrib.auth.views import login, logout



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movie_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^chinna/', include(admin.site.urls)),
    #url(r'^movie_list/$', views.ListView.as_view(), name='movie_index'),
    #url(r'^$', 'MovieLib.views.index'),
    url(r'^$', include('MovieLib.urls', namespace="MovieLib")), #index method inside /MovieLib/views.py will handle the `/` request 
   
    #url(r'^create/$', 'MovieLib.views.Create', name='movie_create'),
    url(r'^index/$', views.ListView.as_view(), name='movie_index'),

    url(r'^create/$', views.CreateView.as_view(), name='movie_create'), 
    url(r'^home/$', views.IndexView.as_view(), name='movie_home'),
    url(r'^movie_list/$', views.ListView.as_view(), name='movie_list'),
    url(r'^edit/(?P<pk>\d+)$', views.UpdateView.as_view(), name='movie_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteView.as_view(), name='movie_delete'),

    url(r'^about_us/$', 'MovieLib.views.about', name='movie_about'),
    url(r'^contact/$', 'MovieLib.views.contact', name='movie_contact'),
   # url(r'^index/$', 'MovieLib.views.logout', name='movie_logout'),
    url(r'^logout/$', 'MovieLib.views.logout', name='movie_logout'),
    url(r'^base_page/$', 'MovieLib.views.base', name='movie_base'),
    #url(r'^movie_list/$', 'MovieLib.views.cancel', name='movie_cancel'),
     
    #url(r'^login/$', 'MovieLib.views.login', name='movie_login'),
  
   # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'MovieLib.views.logout', name='movie_logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^login/$', 'MovieLib.views.login', name='movie_login'),

    url(r'^register/$', 'MovieLib.views.register', name='movie_register'),
    url(r'^register/success/$','MovieLib.views.register_success', name='movie_register'),

    


)

