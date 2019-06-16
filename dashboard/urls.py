from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^check/$', views.check_queries, name='check_queries'),
]