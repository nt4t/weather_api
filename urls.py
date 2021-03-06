from weather import views
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
#urlpatterns = [
#    url(r'^weather/$', views.weather_list),
#    url(r'^weather/(?P<pk>[0-9]+)/$', views.weather_detail),
#]


urlpatterns = [
    url(r'^weather/$', views.WeatherList.as_view()),
    url(r'^weather/(?P<pk>[0-9]+)/$', views.WeatherDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
