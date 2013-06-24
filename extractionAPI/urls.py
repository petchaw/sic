from django.conf.urls import patterns, include, url
from extractionAPI import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<last>\d+)/$', views.getStories, name='getStories'),
)
