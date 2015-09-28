from django.conf.urls import patterns, url
#from MovieLib import views
from MovieLib.views import IndexView, CreateView, UpdateView, DeleteView

from MovieLib import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),

    url(r'^create/$', views.CreateView.as_view(), name='movie_create'),
    url(r'^index/$', views.IndexView.as_view(), name='movie_index'), #new line
    url(r'^movie_list/$', views.ListView.as_view(), name='movie_list'),
   


    url(r'^edit/(?P<pk>\d+)$', views.UpdateView.as_view(), name='movie_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteView.as_view(), name='movie_delete'),
    
   # url(r'^index/$', 'MovieLib.views.logout', name='movie_logout'),
    url(r'^logout/$', 'MovieLib.views.logout', name='movie_logout'),

    url(r'^contact/$', 'MovieLib.views.contact', name='movie_contact'),
    url(r'^about_us/$', 'MovieLib.views.about', name='movie_about'),
    #url(r'^movie_list/$', 'MovieLib.views.cancel', name='movie_cancel'),
   # url(r'^login/$', 'MovieLib.views.login', name='movie_login'),


)
