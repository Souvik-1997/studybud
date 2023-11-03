from django import forms
from base.models.User import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class AuthUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'username':
                visible.field.widget.attrs['placeholder'] = 'e.g. tony_stark'
            else:
                visible.field.widget.attrs['placeholder'] = visible.field.label
            
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
    





