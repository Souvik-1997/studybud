from pprint import pp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from base.forms.RoomForm import RoomForm
from base.models import Message, Room, Topic
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Custom Service object imports
# from base.services.RoomService import room_service_obj

# Custom Service imports
from base.services import RoomService

# Create your views here.


def room(request, pk):
    room = RoomService.roomDetailsById(request, pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    total_participants = participants.count()
    # dd(room_messages) # noqa: F821
    auth_user = request.user
    message = request.POST.get("message")
    if (request.method) == "POST":
        if not message:
            messages.error(request, "Please say somethings!")
            return redirect("room", pk=room.id)
        else:
            message = Message.objects.create(user=auth_user, body=message, room=room)
            room.participants.add(request.user)
            return redirect("room", pk=room.id)
    context = {
        "room": room,
        "room_messages": room_messages,
        "participants": participants,
        "total_participants": total_participants,
    }
    return render(request, "base/pages/rooms.html", context)


@login_required(login_url="login")
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    try:
        if request.method == "POST":
            form_data = RoomForm(request.POST)
            data = RoomService.createNewRoom(request, form_data)
            if isinstance(data, dict):
                context = {"form": form, "topics": topics, "errors": data}
                return render(request, "base/pages/create_room.html", context)
            else:
                messages.success(request, "Room Created successfully.")
                return redirect("home")
    except Exception as e:
        print(e)
    context = {"form": form, "topics": topics}
    return render(request, "base/pages/create_room.html", context)


@login_required(login_url="login")
def updateRoom(request, pk):
    flag = "update"
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.method == "POST":
        if form.is_valid:
            form = RoomForm(request.POST, instance=room)
            form.save()
            messages.success(request, "Room updated successfully.")
            return redirect("home")
    context = {"form": form, "topics": topics, "flag": flag}
    return render(request, "base/pages/create_room.html", context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user == room.host:
        if request.method == "POST":
            room = RoomService.deleteRoomById(pk)
            if room is not None:
                messages.error(request, "Room has been deleted successfully!")
                return redirect("home")
    else:
        messages.error(request, "You have not this permission!")
        return redirect("home")
    room_detail = Room.objects.get(id=pk)
    context = {"room_detail": room_detail}
    return render(request, "base/pages/delete.html", context)


def topics(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    topics = Topic.objects.filter(Q(name__icontains=q))
    # dd(topics) # noqa: F821
    context = {"topics": topics}
    return render(request, "base/pages/topics.html", context)


@login_required(login_url="login")
def deleteMessage(request, pk):
    auth_user = request.user
    message = Message.objects.get(id=pk)

