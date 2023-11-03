from django.http import HttpResponse
from django.shortcuts import redirect, render
from base.models import Message, Room, Topic
from django.db.models import Q

# Custom Service object imports
# from base.services.RoomService import room_service_obj

# Custom Service imports
from base.services.RoomService import RoomService

# Create your views here.


def home(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    page = request.GET.get("page", 1)
    rooms_obj = RoomService.pagination(request, page, rooms)
    rooms_count = Room.objects.count()
    topics = Topic.objects.all()[:5]
    all_messages = Message.objects.all()
    room_data = []

    for room in rooms_obj:
        participants_count = room.participants.count()
        room_data.append(
            {"room": room, "participants_count": participants_count}
        )
                      
    context = {
        "topics": topics,
        "rooms_data": room_data,
        "rooms": rooms_obj,
        "rooms_count": rooms_count,
        "all_messages": all_messages,
    }

    return render(request, "base/home.html", context)
