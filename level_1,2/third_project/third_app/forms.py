from django import forms
from third_app.models import User
from django.core import validators
class NewUserForm(forms.ModelForm):
    first_name = forms.CharField(validators = [validators.MaxLengthValidator(0)])
    last_name = forms.CharField()
    email = forms.EmailField()
    

    class Meta():
        model = User
        fields = '__all__'
