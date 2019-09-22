# pylint: disable=no-member

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app1.models import AccessRecord, Topic, Webpage
from app1.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import forms
# Create your views here.

def index(request):
    lista_paginas = AccessRecord.objects.order_by('date')
    dict_paginas = {'access_records': lista_paginas}
    return render(request, 'app1/index.html', context=dict_paginas)

def form_name_view(request):
    '''
    Formulario de prueba
    '''
 
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validacion exitosa')
            print('name: '+form.cleaned_data['name'])
            print('email: '+form.cleaned_data['email'])
            print('texto: '+form.cleaned_data['text'])

    formulario = {'form': form}
    return render(request, 'app1/forms_page.html', formulario)

def form_register_view(request):
    '''
    Formulario de registro
    '''
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    formulario = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'app1/registration.html', formulario)


def user_login(request):
    '''
    Login de usuario
    '''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Cuenta inactiva')
        
        else:
            print('usuario intenta contectarse')
            print('usuario: {} ... pass: {}'.format(username, password))
            return HttpResponse('Detalles de ingreso incorrectos')
        
    else:
        return render(request, 'app1/login.html', {})

@login_required
def user_logout(request):
    '''
    Desconexion de cuenta
    '''
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    '''
    Mensaje de ingreso
    '''
    return HttpResponse('Conectado')