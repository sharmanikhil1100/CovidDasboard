from django.http import HttpResponse
from django.shortcuts import render
from .models import CovidData
import json

encoding = 'utf-8'

def index(request):
    states = ['gujarat, maharashtra, andhra pradesh']
    return render(request, 'covid/get-all', {
        'state': states,
    }
    )

def get_data(request):
    if request.method=="GET":
        # x = CovidData.objects.all()
        # return json.loads(x)
        data = str(request.body, encoding)
        covidData=CovidData()
        query_result = []

        for p in CovidData.objects.raw('SELECT * FROM covid_covidData'):
            query_result.append(p)
        return render(request, 'home/home.html', {
            'state_data':query_result
        })
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