from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .filters import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def getAllCar(request):
    car=Car.objects.all()   # (Get a list of all cars)
    filter=carFilter(request.GET,queryset=Car.objects.all().order_by("id"))  #Apply filtering based on request parameters
    serializer=carSerializer(filter.qs,many=True)       # Serialize the filtered cars and return the response
    return Response(serializer.data)

#here create the api that get data by id
@api_view(["GET"])
def getById(request,id):
    car=get_object_or_404(Car,pk=id)   # Get a car by its unique ID or return a 404 error if not found
    serializer=carSerializer(car,many=False)  
    return Response(serializer.data)

#this one is the post api that add record of newcar
@api_view(["POST"])
def addNewCar(request):
    data=Car() # Create a new Car instance and populate it with data from the request
    data.owner_name=request.data.get("owner_name")
    data.car_model=request.data.get("car_model")
    data.color=request.data.get("color")
    data.price=int(request.data.get("price"))
    data.year=int(request.data.get("year"))
    data.save()  # Save the new car instance to the database
    serializer=carSerializer(data,many=False)
    return Response({"message":"car created sucessfully"})

# it update the already existing record 
@api_view(["PUT"])
def updateCar(request,id):
    car=get_object_or_404(Car,pk=id)
    # Update the car's attributes based on the request data
    car.owner_name=request.data["owner_name"]
    car.car_model=request.data["car_model"]
    car.color=request.data["color"]
    car.price=int(request.data["price"])
    car.year=int(request.data["year"])
    # Save the updated car (you can uncomment this if you want to save changes)
    #car.save()  
    serializer=carSerializer(car,many=False)
    return Response(serializer.data)

# this api is to delete the record of the cars
@api_view(["DELETE"])
def deleteCar(request,id):
    car=get_object_or_404(Car,pk=id)
    car.delete()
    return Response({"message":"record of car is deleted successfully"})
