from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
peoples = [{"name":"Ravi Kumar", "age":18},{"name":"Ivan Kumar", "age":8},{"name":"Prakash Kumar", "age":18} ]
def home(request):
    return render(request, "index.html", context={"people":peoples})
def sucess(request):
    return HttpResponse("This page is render sucessfully")