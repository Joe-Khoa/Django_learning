from django import forms
from django.core import validators
from first_app.models import User



################################## botcacher ##################################
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.validationError("NAME MUST START BY Z")


class FormName(forms.ModelForm):
    # name  = forms.CharField(validators=[check_for_z])
    # name  = forms.CharField()
    email = forms.EmailField()
    # text = forms.CharField(widget=forms.Textarea)

    ################################## botcacher smarter ##################################
    botcacher = forms.CharField(required=False,
                                widget = forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)])


################################## botcacher ##################################
    botcacher = forms.CharField(required=False,
                                widget = forms.HiddenInput)
    def clean_botcatcher(self):
        botcacher  = self.cleaned_data['botcacher']
        if len(botcacher) > 0:
            print('catched bot!')
            raise forms.validationError("You a bot ")
        return botcacher
    class Meta:
        model = User
        fields = '__all__'

#
# google.ipo
# blue@123.vn
# superhero
