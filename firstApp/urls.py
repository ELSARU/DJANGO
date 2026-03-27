from django.urls import path
from . import views
from .views import home


urlpatterns = [

    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    



    
    path('', views.home, name='home'), 
    
    path('create-ocean', views.createOcean, name="create-ocean"),
    path('read-oceans', views.readOceans, name="read-oceans"),
    path('read-ocean/<str:pk>', views.readOcean, name="read-ocean"),
    path('update-ocean/<str:pk>', views.updateOcean, name="update-ocean"),
    path('delete-lake/<str:pk>', views.deleteOcean, name="delete-ocean"),

    path('create-lake', views.createOcean, name="create-lake"),
    path('read-lakes', views.readOcean, name="read-lakes"),
    path('read-lake/<str:pk>', views.createOcean, name="read-lake"),
    path('update-lake/<str:pk>', views.updateOcean, name="update-lake"),
    path('delete-lake/<str:pk>', views.deleteOcean, name="delete-lake")
]