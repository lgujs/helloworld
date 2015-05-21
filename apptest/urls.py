__author__ = 'Administrator'


from django.conf.urls import patterns, include, url
from apptest import views
from django.views.generic import DetailView, ListView
from apptest.models import Poll, Choice


urlpatterns = patterns('apptest.views',

#   url('^$', views.poll_index, name='index'),
#   url(r'^(\d+)/$', views.detail, name='poll_detail'),
#   url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='apptest/index.html'),
        name='index'),

    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            context_object_name='tpoll',
            template_name='apptest/detail.html'),
        name='detail'),

    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='apptest/results.html'),
        name='results'),


)