from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.contrib.auth.models import User
from django .contrib.auth import authenticate
from django.urls import reverse_lazy
# Create your views here.

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            User.objects.create_user(username=username, email='' ,password=password)
            user = authenticate(username=username, password=password)
            if user is not None:
                response =  redirect('login')
                response.delete_cookie()
                return response

    else:
            form = CadastroForm()
    return render(request, 'cadastro.html', {'form':form})
