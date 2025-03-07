from django.contrib import admin
from principal.models import cadastro

class AdminPrincipal(admin.ModelAdmin):
    list_display = ('nome', 'cnpj') #lista de campos na tabela
    search_fields = ('nome', 'cnpj') #campo de busca

admin.site.register(cadastro, AdminPrincipal) #função que liga a tabela ao admin