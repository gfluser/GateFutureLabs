from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blog/', views.blog, name='blog'),
    path('details/', views.details, name='details'),
    path('join/', views.join, name='join'),
    path('summary/', views.summary, name='summary'),


]