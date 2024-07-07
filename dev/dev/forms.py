from django.forms import ModelForm
from mainapp.models import Rooms

class RoomForm(ModelForm):
    class Meta:
        model=Rooms
        fields='__all__'
