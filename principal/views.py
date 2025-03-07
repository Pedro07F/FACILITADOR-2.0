from principal.models import cadastro
from django.shortcuts import render

def principal_view(request):
    return render(request, 'cadastro.html') # O Render renderiza uma resposta Http e devolve o template
