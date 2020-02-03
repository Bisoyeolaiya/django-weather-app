from django.conf.urls import url
from . import views

app_name = 'weather'


urlpatterns = [
    url(r'^delete/(?P<city_name>\D+)/', views.delete_city, name='delete_city'),
    url(r'^$', views.index, name='index'),
]
