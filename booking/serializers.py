from rest_framework import serializers
from . import models



class HotelsAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = "__all__"


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelImage
        fields = "__all__"
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"



class EventAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventImage
        fields = "__all__"