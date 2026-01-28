from django.shortcuts import render

def std(request):
    return render(request, 'studentsapp/home.html')

def detail(request):
    return render(request, 'studentsapp/detail.html')

def about(request):
    return render(request, 'studentsapp/about.html')