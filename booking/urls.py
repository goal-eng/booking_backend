from django.urls import path , include
from . import views


urlpatterns = [
    path('hotel/',views.HotelAddView.as_view()),
    path('hotel/<int:pk>/',views.HotelAddView.as_view()),
    path('hotel_image/',views.HotelImagesView.as_view()),
    path('event/',views.EventAddView.as_view()),
    path('event/<int:pk>/',views.EventAddView.as_view()),
    path('event_image/',views.EventImagesView.as_view()),

    path('booking/',views.HotelBooking.as_view()),
    # path('booking/',views.HotelBooking.as_view()),

    
]