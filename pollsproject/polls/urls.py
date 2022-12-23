from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.detail, name='detail'),
    path('<str:pk>/results/', views.results, name='results'),
    path('<str:pk>/vote/', views.vote, name='vote'),

]
