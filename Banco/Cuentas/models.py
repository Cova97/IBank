from django.db import models

# Create your models here.
class Usuario:
    def __init__(self, name, email, clabe):
        self.name = name
        self.email = email
        self.clabe = clabe