from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^hist/', views.hist, name='hist'),

#    url(r'^hist/', views.hist, name='hist'),

#    url(r'^accounts/login/$',  login),
#    url(r'^accounts/logout/$', logout),
]
