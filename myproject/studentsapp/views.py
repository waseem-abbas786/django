from django.shortcuts import render

def std(request):
    return render(request, 'studentsapp/home.html')

def detail(request):
    return render(request, 'studentsapp/detail.html')
