from django.shortcuts import redirect
from base.models import Room


class RoomRepository:
    
    def createRoomRepository(data):
        room = Room.objects.create(
            host = data['host'],
            name = data["name"],
            topic = data["topic"],
            description = data["description"],
        )
        if room is not None:
            return room

    def deleteRoom(data):
        data.delete()
        return {1 : '1'}
