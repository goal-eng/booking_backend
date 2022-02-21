from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import permissions
from rest_framework import status
from . import serializers
from . import models
from user_auth.utils import get_response , manager_access


class HotelAddView(APIView):
    permission_classes =[permissions.IsAuthenticated,manager_access,]
    def get(self,request):
        object=models.Hotel.objects.all()
        pk=request.GET.get("Hotel_id")
        if pk:
            HotelObj=object.filter(pk=pk)
        else:
            HotelObj=object
        serializer=serializers.HotelsAddSerializer(HotelObj,many=True).data
        message="Hotel data"
        return Response(get_response(200,message,serializer))

    def post(self,request):
        serializer=serializers.HotelsAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message="Hotel added successfully"
            return Response(get_response(200,message,serializer.data))
        message="field error"
        return Response(get_response(400,message,serializer.errors))

    def patch(self,request,pk):
        try:
            object=models.Hotels.objects.get(pk=pk)
            serializer=serializers.HotelsAddSerializer(object,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                message="Hotel updated successfully"
                return Response(get_response(200,message,serializer.data))
            message="field error"
            return Response(get_response(400,message,serializer.errors))
        except:
            message="Hotel not found"
            return Response(get_response(404,message))
            
    def delete(self,request,pk):
        object=models.Hotels.objects.filter(pk=pk)
        if object.exists():
            object.delete()
            message="Hotel removed"
            return Response(get_response(200,message))
        else:
            message="Hotel not found"
            return Response(get_response(404,message))

class HotelImagesView(APIView):
    permission_classes =[permissions.IsAuthenticated,manager_access,]
    def get(self,request,pk):
        object=models.HotelImage.objects.filter(pk=pk)
        serializer=serializers.HotelImageSerializer(object,many=True).data
        message="Hotel images"
        return Response(get_response(200,message,serializer.data))

    def post(self,request):
        serializer=serializers.HotelImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message="Hotel image added successfully"
            return Response(get_response(200,message,serializer.data))
        message="field error"
        return Response(get_response(400,message,serializer.errors))


class EventAddView(APIView):
    permission_classes =[permissions.IsAuthenticated,manager_access,]
    def get(self,request,pk):
        object=models.Event.objects.all()
        hotel_id=request.GET.get("Hotel_id")
        event_id=request.GET.get("event_id")
        if hotel_id:
            eventObj=object.filter(hotel_id=hotel_id)
        if event_id:
            eventObj=object.filter(pk=event_id)
        else:
            eventObj=None
        serializer=serializers.EventAddSerializer(eventObj,many=True).data
        message="Hotel data"
        return Response(get_response(200,message,serializer.data))

    def post(self,request):
        serializer=serializers.EventAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message="Hotel added successfully"
            return Response(get_response(200,message,serializer.data))
        message="field error"
        return Response(get_response(400,message,serializer.errors))

    def patch(self,request,pk):
        try:
            object=models.Event.objects.get(pk=pk)
            serializer=serializers.EventAddSerializer(object,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                message="Event updated successfully"
                return Response(get_response(200,message,serializer.data))
            message="field error"
            return Response(get_response(400,message,serializer.errors))
        except:
            message="Hotel not found"
            return Response(get_response(404,message))
            
    def delete(self,request,pk):
        object=models.Event.objects.filter(pk=pk)
        if object.exists():
            object.delete()
            message="Event removed"
            return Response(get_response(200,message))
        else:
            message="Event not found"
            return Response(get_response(404,message))

class EventImagesView(APIView):
    permission_classes =[permissions.IsAuthenticated,manager_access,]
    def get(self,request,pk):
        object=models.EventImage.objects.filter(pk=pk)
        serializer=serializers.EventImageSerializer(object,many=True).data
        message="Hotel images"
        return Response(get_response(200,message,serializer.data))

    def post(self,request):
        serializer=serializers.EventImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message="Hotel image added successfully"
            return Response(get_response(200,message,serializer.data))
        message="field error"
        return Response(get_response(400,message,serializer.errors))

class HotelBooking(APIView):
    def post(self,request):
        event=request.data.get("event_id")
        start_day=request.data.get("start_day")
        end_day=request.data.get("end_day")
        if event is None:
            message="event field required"
            return Response(get_response(400,message))
        if start_day is None:
            message="start_day field required"
            return Response(get_response(400,message))
        if end_day is None:
            message="end_day field required"
            return Response(get_response(400,message))
        time_check=models.Booking.objects.filter(event=event)
        if not time_check.exists():
            message="event not found"
            return Response(get_response(404,message))
        check_1 = time_check.filter(start_day__lte=start_day, end_day__gte=start_day).exists()
        check_2 = time_check.filter(start_day__lte=end_day, end_day__gte=end_day).exists()
        check_3 = time_check.filter(start_day__gte=start_day, end_day__lte=end_day).exists()
        if check_1 or check_2 or check_3:
            message="Hotel is not avaliable"
            return Response(get_response(400,message))
        serializer=serializers.BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message=f"Hotel :{event} booked successfully"
            return Response(get_response(200,message,serializer.data))
        message="field error"
        return Response(get_response(400,message,serializer.errors))