from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Tabla
# Create your views here. CONTROLLER    

def tabla_list(request):
    lista = Tabla.objects.order_by('Fecha')
    return render(request, 'hoteles/hoteles_list.html', {'hoteles':lista})