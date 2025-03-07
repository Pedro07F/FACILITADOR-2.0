from django.shortcuts import render
from principal.models import cadastro
from django.http import HttpResponse

def principal_view(request):
    '''empresas = cadastro.objects.all()
    return render(request,'cadastro.html',{'cadastro':cadastro})'''
    return HttpResponse('Meus Carros')
