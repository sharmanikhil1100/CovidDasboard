from django.http import HttpResponse
from .models import CovidData

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_data(request):
    if request.method=="GET":
        return HttpResponse("Data!")
    return HttpResponse("Invalid Request", status=400)

def insert(request):
    if request.method=="POST":
        covidData=CovidData()
        covidData.patient_no=1
        covidData.city="c1"
        covidData.state="s1"
        covidData.date="d1"
        covidData.save()
        return HttpResponse("Data Inserted!")
    return HttpResponse("Invalid Request", status=400)