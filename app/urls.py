# app/urls.py

from django.urls import path

from .views import post_list_view, post_detail_view

app_name = 'app'

urlpatterns = [
    path('', post_list_view, name='list'),
    path('<int:id>/', post_detail_view, name='detail'),
]
