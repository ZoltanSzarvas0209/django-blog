from django.shortcuts import render
from .models import Practise

# Create your views here.

def practise_one(request):
    practise = Practise.objects.all().order_by('created_on').first()

    return render(
        request, 
        "practise/practise.html",
        {"practise":practise},
        )
