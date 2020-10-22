from django.http import HttpResponse
from django.shortcuts import render
from .models import CovidData
from django.core.serializers import serialize
import json

encoding = 'utf-8'

def index(request):
    states = ['gujarat, maharashtra, andhra pradesh']
    return render(request, 'covid/get-all', {
        'state': states,
    }
    )

def home(request):
    return render(request, 'home/home.html', {"data_rows":json.loads(get_all_data())} )

def get_data(request):
    if request.method=="GET":                
        # for entry in query_result:
        #     print(entry['pk'])        
        # return HttpResponse(get_all_data())
        return render(request, 'home/home.html', {"data_rows":json.loads(get_all_data())} )
    return HttpResponse("Invalid Request", status=400)

def get_all_data():
    return serialize('json', CovidData.objects.all())

def insert(request):
    if request.method=="POST":
        print(request.POST)
        input_data=request.POST
        covidData=CovidData()
        covidData.patient_no=input_data["patient_no"]
        covidData.city=input_data["city"]
        covidData.state=input_data["state"]
        covidData.date=input_data["date"]
        covidData.save()
        return render(request, 'home/home.html', {"data_rows":json.loads(get_all_data())} )
    return HttpResponse("Invalid Request", status=400)