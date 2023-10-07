from django.http import HttpResponse
from django.shortcuts import redirect
from base.models import Room
from django.core.paginator import Paginator

# Custom configuration import
from base.configuration.Config import Config

# Custom repository import
from base.repository.RoomRepository import RoomRepository


class RoomService:
    def roomDetailsById(request, pk) -> Room:
        room_details = Room.objects.get(id=pk)
        return room_details

    def createNewRoom(request, form_data):
        auth_user = request.user
        try:
            if form_data.is_valid():
                name = form_data.cleaned_data["name"]
                topic = form_data.cleaned_data["topic"]
                description = form_data.cleaned_data["description"]
                room_data = {
                    "host": auth_user,
                    "name": name,
                    "topic": topic,
                    "description": description,
                }
                data = RoomRepository.createRoomRepository(room_data)
                if data is not None:
                    return data
            else:
                data = form_data.errors
                return data
        except Exception as e:
            print(e)
            
            
    def deleteRoomById(pk):
        try:
            room_obj = Room.objects.get(id=pk)
            if room_obj is not None:
                room = RoomRepository.deleteRoom(room_obj)
                return room
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    # pagination
    def pagination(request, page, obj):
        paginator = Paginator(obj, Config.PAGE_LIMIT_CONSTANT)
        rooms_obj = paginator.page(page)
        return rooms_obj



# room_service_obj = RoomService()
