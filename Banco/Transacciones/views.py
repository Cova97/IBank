from django.shortcuts import render, get_object_or_404
from .models import Cuenta

# Create your views here.
def depositar(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, pk=cuenta_id)
    if request.method == 'POST':
        monto = float(request.POST['monto'])
        cuenta.depositar(monto)
    return render(request, 'depositar.html', {'cuenta': cuenta})

def retirar(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, pk=cuenta_id)
    if request.method == 'POST':
        monto = float(request.POST['monto'])
        cuenta.retirar(monto)
    return render(request, 'retirar.html', {'cuenta': cuenta})
