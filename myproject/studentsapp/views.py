from django.shortcuts import render

def std(request):
    return render(request, 'studentsapp/home.html')
