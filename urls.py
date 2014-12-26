from django.conf.urls import url
from weather import views

urlpatterns = [
    url(r'^weather/$', views.weather_list),
    url(r'^weather/(?P<pk>[0-9]+)/$', views.weather_detail),
]
