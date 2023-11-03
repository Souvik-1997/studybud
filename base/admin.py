from django.contrib import admin
from base.models.Room import Room
from base.models.Topic import Topic
from base.models.Message import Message
from base.models.User import User

# Register your models here.


# class RoomAdmin(admin.ModelAdmin):
#     list_display = ("name", "description", "host", "topic", "updated_at", "created_at")
#     search_fields = ("name__startswith", "description__startswith")
#     # list_filter = ("update")


# class MessageAdmin(admin.ModelAdmin):
#     list_display = ("body", "user", "room", "updated_at", "created_at")


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
