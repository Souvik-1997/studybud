from django.contrib import admin
from base.models.Room import Room
from base.models.Topic import Topic
from base.models.Message import Message

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "host", "topic", "update", "create")
    search_fields = ("name__startswith", "description__startswith")
    # list_filter = ("update")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("body", "user", "room", "update", "create")


admin.site.register(Room, RoomAdmin)
admin.site.register(Topic)
admin.site.register(Message, MessageAdmin)
