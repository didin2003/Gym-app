
from django.urls import path
from fitnessapp import views
urlpatterns = [
     path('',views.Home,name="Home"),
     path('signup',views.signup,name="signup"),
     path('login',views.handlelogin,name="handlelogin"),
     path('logout',views.handlelogout,name="handlelogout"),
     path('contact',views.contact,name="contact"),
     path('join',views.enroll,name="enroll"),
     path('profile',views.profile,name="profile"),
     path('attendance',views.attendance,name="attendance"),
     path('gallery',views.gallery,name="gallery"),
     path('about',views.about,name="about"),
]
