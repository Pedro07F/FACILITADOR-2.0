from django.db import models

# Create your models here.
class cadastro(models.Model):
    nome = models.CharField(max_length=200) #Campo obrigatório
    cnpj = models.CharField(max_length=14, blank=True, null= True) #Pode ser deixado em branco no formulário e salvo como NULL

    def __str__(self):
        return self.nome #metodo que mostra o objeto como texto