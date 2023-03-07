from django.db import models

# Create your models here.
class Cuenta(models.Model):
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def depositar(self, monto):
        self.saldo += monto
        self.save()

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            self.save()
