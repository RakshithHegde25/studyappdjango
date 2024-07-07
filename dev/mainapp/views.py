from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import Rooms
from dev.forms import RoomForm

# rooms=[

#     {"id":1,"name":"Rakshith"},
#     {"id":2,"name":"Somerandom"},
#     {"id":3,"name":"Yes"},
#     {"id":4,"name":"Nope"},
# ]

def home(request):
    rooms=Rooms.objects.all()
    return render(request,'homepage.html',{"rooms":rooms})

def createroom(request):
     form=RoomForm()
     context={"form":form}
     if request.method=='POST':
          form=RoomForm(request.POST)
          if form.is_valid():
               form.save()
    
     return render(request,'roomform.html',{"form":form})






# Create your views here.
