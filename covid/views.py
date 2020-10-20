from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_data(request):
    if request.method=="GET":
        return HttpResponse("Data!")
    return HttpResponse("Invalid Request", status=400)

def insert(request):
    if request.method=="POST":
        return HttpResponse("Data Inserted!")
    return HttpResponse("Invalid Request", status=400)