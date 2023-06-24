from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('Завтрак', views.zavtrak, name="zavtrak"),
    path("Завтрак/<int:zavtrak_id>/", views.zavtrak_detail, name="zavtrak_details"),
    path('Обед', views.obed, name="obed"),
    path("Обед/<int:obed_id>/", views.obed_detail, name="obed_details"),
    path('Ужин', views.uzhin, name="uzhin"),
    path("Ужин/<int:uzhin_id>/", views.uzhin_detail, name="uzhin_details"),
    path('Логин', views.login, name="login"),
]
