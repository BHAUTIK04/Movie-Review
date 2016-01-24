from django.conf.urls import url
from smr import views

urlpatterns = [
	url(r'^$',views.home),
    url(r'^movies/$', views.list),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.detail),
    url(r'^movie/$', views.movie_list),
    url(r'^movie/(?P<pk>[0-9]+)/$', views.movie_detail),
]