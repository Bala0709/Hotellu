from django.urls import path
from hotellu_app import views

#TEMPLATE TAGGING

app_name = 'hotellu_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user_index, name = 'user_index'),
    path('form_page', views.form_page, name = 'form_page'),
    path('user_form', views.user_form, name= 'user_form'),
    path('base', views.base_html, name = 'base'),
    path('other', views.other_html, name = 'other'),
    path('relative_url_path', views.relative_html, name = 'relative'),
    path('register', views.register_html, name='register'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
]
