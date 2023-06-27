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
    path('login', views.login, name="login"),
    path('login/registration', views.login_reg, name="login_reg"),
    path('login/sign_in', views.login_login, name="login_login"),
    path('login/sign_in/complete', views.login_login_, name="login_sign_in"),
    path("login/registration/complete", views.login_reg_, name="login_check"),
    path("poisk/", views.poisk_str, name="poisk_str"),

]
