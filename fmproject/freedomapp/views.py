from django.shortcuts import render
from.models import place,team
# Create your views here.
def freedom(request):
    obj=place.objects.all()
    bnb=team.objects.all()
    return render(request,"index.html",{'result':obj,'found':bnb})
