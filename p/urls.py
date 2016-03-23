from django.conf.urls import url

from . import views

app_name = 'p'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'map/$', views.mapdisplay, name='map'),

]
