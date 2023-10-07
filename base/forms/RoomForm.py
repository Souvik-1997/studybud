from django import forms
from base.models import Room
from django.core.exceptions import ValidationError

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        topic = cleaned_data.get('topic')
        description = cleaned_data.get('description')

        if not name and not topic and not description:
            raise ValidationError("Please enter a name, topic, and description.")   