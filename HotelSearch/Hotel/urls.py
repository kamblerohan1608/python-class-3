from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hotel_api/',views.hotel_api,name='hotel_api'),
    path('hotel_details/',views.hotel_details,name='hotel_details'),
]
