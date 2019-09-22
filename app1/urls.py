# from django.urls import path
from django.conf.urls import url
from app1 import views

app_name = "app1"


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form_page/', views.form_name_view, name='formulario_1'),
    url(r'^register/', views.form_register_view, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
