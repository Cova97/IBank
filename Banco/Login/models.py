from django.db import models

# Create your models here.
class Logig:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Signin:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email