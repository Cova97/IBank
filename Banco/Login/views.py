from django.shortcuts import render
from .models import Logig, Signin

# Create your views here.
def create_loging():
    nombre = str(input('Dame un nombre'))
    contraseña = str(input('Dame tu contraseña'))
    
    loging = Logig(nombre, contraseña)
    print(loging)

def create_singin():
    nombre = str(input('Dame un nombre'))
    contraseña = str(input('Dame tu contraseña'))
    correo = str(input('Dame un correo'))
    
    singin = Signin(nombre, contraseña, correo)
    print(singin)
