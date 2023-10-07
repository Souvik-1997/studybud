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
    # dd(request)  # noqa: F821
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    # dd(rooms) # noqa: F821
    page = request.GET.get("page", 1)
    rooms_obj = RoomService.pagination(request, page, rooms)
    # dd(rooms_obj) # noqa: F821
    rooms_count = Room.objects.count()
    topics = Topic.objects.all()
    all_messages = Message.objects.all().order_by("-create")[:3]
    import os
    print('===> Current file path:', os.path.abspath(__file__))
    print('===> Debugging...> ', all_messages)
    context = {
        "topics": topics,
        "rooms": rooms_obj,
        "rooms_count": rooms_count,
        "all_messages": all_messages,
    }

    return render(request, "base/home.html", context)
