from django.urls import path
from .views import*
urlpatterns = [
    path("get",getAllCar),   
    path("get/<str:id>",getById), 
    path("post",addNewCar),
    path("put/<str:id>",updateCar),
    path("delete/<str:id>",deleteCar)
]
