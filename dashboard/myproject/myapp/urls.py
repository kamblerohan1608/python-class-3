from django.urls import path
from . import views



urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
    path('dashboard/',views.dashboard.as_view(),name='dashboard'),
    path('signout/',views.signout.as_view(),name='signout'),
    path('blogs/',views.blogs.as_view(),name='blogs'),

]