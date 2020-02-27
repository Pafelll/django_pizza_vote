from django.urls import path, include

from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register('pizza', views.PizzaView, basename='pizza')

urlpatterns = [
    path('api/', include(routers.urls)),
    path('vote/', views.vote_view, name='vote_view'),
    path('result/', views.result_view, name='result_view'),
]