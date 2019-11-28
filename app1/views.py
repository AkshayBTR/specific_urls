from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def home_project(request):
    return render(request,'home_project.html')