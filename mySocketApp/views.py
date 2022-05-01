from django.shortcuts import render

from mySocketApp.models import Message

# Create your views here.
def index(request):
    messages=Message.objects.all()
    context={"messages": messages}
    return render(request, 'mySocketApp/index.html', context)

def room(request, room_name):
    messages=Message.objects.all()
    return render(request, 'mySocketApp/room.html', {
        'room_name': room_name,
        'messages': messages
    })