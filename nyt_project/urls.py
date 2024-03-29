from django.conf.urls import patterns, include, url
from django.contrib import admin
from extractionAPI import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stories/(?P<last>\d+)/$', views.getStories, name='getStories'),
    url(r'^story/(?P<story_id>\d+)/$', views.getStory, name='getStory'),
    url(r'^storiesbytag/(?P<tag>\w+)/(?P<cnt>\d+)/$', views.getStoriesByTag, name='getStoriesByTag'),
)