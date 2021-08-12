from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("Home/",views.IndexPage,name="homepage"),
    path("Register-Page/",views.RegisterPage,name="regpage"),
    path("Registration/",views.Register,name="Registerdata"), 
    path("Updaate-Page/<int:pk>",views.UpdatePage,name="updatepage"),
    path("Updaate/<int:pk>",views.Update,name="update"),
    path("Delete/<int:pk>",views.Delete,name="delete"),
    path('',views.LoginPage,name='loginpage'),
    path('Login-User/',views.LoginUser,name='loginuser'),
    path('Logout/',views.LogOut,name='logout'),
]
