from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/", views.room, name="room"),
    path("test_func/", views.test_func, name="test_func"),
    path("get_response/", views.get_response, name="get_response"),
]