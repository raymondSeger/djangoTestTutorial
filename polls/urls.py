from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url
from . import views

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # ex: /polls/
        url(r'^$', views.index, name='index'),
        # ex: /polls/5/
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        # ex: /polls/5/results/
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
        # ex: /polls/5/vote/
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]