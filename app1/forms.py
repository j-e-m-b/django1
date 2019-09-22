from django import forms
from django.core import validators
from django.contrib.auth.models import User
from app1.models import UserProfileInfo


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("debe empezar con z")

class FormName(forms.Form):
    '''
    Formulario
    '''
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='ingresa email otra vez')
    text = forms.CharField(widget=forms.Textarea)

    #Esto evita que bots o usuarios modifiquen el html e inserten "values" en los "input"
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput, 
                                 validators=[validators.MaxLengthValidator(0)])

    # debe tener ester formato "clean_'catcher'""

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("los correos deben coincidir")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Modificacion de codigo detectada')
    #     return botcatcher


class UserForm(forms.ModelForm):
    '''
    Formulario de registro de usuarii
    '''
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    '''
    Formulario de perfil de usuario
    '''
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'profile_pic')
        