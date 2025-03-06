from django.shortcuts import render
from principal.models import cadastro

def principal_view(request):
    empresas = cadastro.objects.all()
    return render(request,'cadastro.html',{'cadastro':cadastro})

