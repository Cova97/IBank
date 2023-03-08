from django.db import models

# Create your models here.
class Usuario:
    def __init__(self, name, age, email, clabe):
        self.name = name
        self.age = age
        self.email = email
        self.clabe = clabe