from django.http import HttpResponse
from .models import CovidData
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_data(request):
    if request.method=="GET":
        # x = CovidData.objects.all()
        # return json.loads(x)
        return HttpResponse("Data!")
    return HttpResponse("Invalid Request", status=400)

def insert(request):
    if request.method=="POST":
        input_data=json.loads(request.body)        
        covidData=CovidData()
        covidData.patient_no=input_data["patient_no"]
        covidData.city=input_data["city"]
        covidData.state=input_data["state"]
        covidData.date=input_data["date"]
        covidData.save()
        return HttpResponse("Data Inserted!")
    return HttpResponse("Invalid Request", status=400)