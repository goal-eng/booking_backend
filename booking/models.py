from email.mime import image
from django.db import models
from user_auth.models import CustomUser

from datetime import date


class Hotel(models.Model):
    manager=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="manager")
    name=models.CharField(max_length=200)
    hotel_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    address_line1=models.CharField(max_length=200)
    address_line2=models.CharField(max_length=200)
    pincode=models.IntegerField()
    no_of_days_advance=models.IntegerField()
    start_date=models.DateField(auto_now=False, auto_now_add=True)
    hotel_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    def __str__(self):
        return self.id

class HotelImage(models.Model):
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)

class Event(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="hotelEvent")
    name=models.CharField(max_length=200)
    price=models.FloatField(default=10000)
    limit=models.IntegerField(default=20)

class EventImage(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name="eventImages")
    event_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)

class Booking(models.Model):
    # hotel_no=models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name="hotel")
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name="eventName")
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="Customer")
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    end_day=models.DateField(auto_now=False, auto_now_add=False)
    amount=models.FloatField()
    booked_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.id
    


