from django.shortcuts import render
from .models import Usuario
# Create your views here.

def create_user():
    nombre = str(input('Dame un nombre: '))
    correo = str(input('Dame un correo: '))
    clave = int(input('Dame una nueva clave: '))

    user = Usuario(nombre, correo, clave)
    print(user)



