from django.urls import path
from . import views
from django.conf import settings
from .views import *
from django.conf.urls.static import static

# By Sarikaya

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
 
    path('verify_email/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),
    # path('verify_email_sent/', views.verify_email_sent, name='verify_email_sent'),
    path('register_success/', views.register_success, name='register_success'),
    

]