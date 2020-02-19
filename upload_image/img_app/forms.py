from django import forms
from img_app.models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name','hotel_img']
