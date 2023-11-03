from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from base.models import Message


def message_delete_permission(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Do something before the function.
        auth_user = request.user
        message_id = kwargs.get("pk")
        message = Message.objects.get(id=message_id)
        if (auth_user == message.user) or (auth_user == message.room.host):
            return view_func(request, *args, **kwargs)
        # Do something after the function.

    return wrapper_func
