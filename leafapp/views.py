from django.shortcuts import render
from .models import Place,People
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    pi = People.objects.all()
    return render(request,"index.html",{'result':obj,'answer':pi})

#def plate(request):

  # return render(request,"index.html")
