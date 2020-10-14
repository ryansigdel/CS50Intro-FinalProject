from django.urls import path,include 
from . import views
from .views import Home,Comment



urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register,name="register"),
    path('create_post/',views.createPost,name="create"),
    path('',Home.as_view(),name='home'),
    path('comments/id=<str:pk_second>/' , views.view_blog , name = 'view_comment'),
    path('profile/',views.profile,name="profile")


]