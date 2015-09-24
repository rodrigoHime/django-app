from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import *

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^entry/create/$', EntryCreate.as_view(), name='entry_create'),
    url(r'^entry/edit/(?P<pk>\d+)/$', EntryUpdate.as_view(), name='entry_update'),
    url(r'^entry/delete/(?P<pk>\d+)/$', EntryDelete.as_view(), name='entry_delete'),
    url(r'^entry/search/$', search_entries, name='search_entries'),
    url(r'^log/$', LogList.as_view(), name='log_list'),
)
