from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url
from . import views

app_name = 'polls'
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]