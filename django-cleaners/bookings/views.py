from django.shortcuts import render

# Create your views here.

def MyView(request):
    return render(request, "main/my.html")