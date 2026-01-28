from django.shortcuts import render

def std(request):
    return render(request, 'studentsapp/home.html')

def about(request):
    return render(request, 'studentsapp/about.html')