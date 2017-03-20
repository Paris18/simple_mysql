from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^usr_info', views.get_details,name = 'details'),
    url(r'^usrs', views.getlist,name = 'usr_list'),
    url(r'^register', views.register,name = 'register'),
]