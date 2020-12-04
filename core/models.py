from django.db import models
from django.contrib.auth.models import User  # Importa os modulos do Django no caso o User

# Create your models here.

class Evento(models.Model):  # Criamos a classe que cria a tabela
    titulo = models.CharField(max_length=100)   # Criamos o campo titulo do tipo char  com tamaho 100
    descricao = models.TextField(blank=True, null=True) # Criamos o campo descrição do tipo podendo ser nulo (em branco)
    data_evento = models.DateTimeField(verbose_name='Data do Evento') # Criamos o campo data do evento do tipo Date
    data_criacao = models.DateTimeField(auto_now=True) # Criamos o campo data da criacao com a data corrente
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Se o usuario dono do evento for deletado todos os demais registros referentes a ele serao apagados

    class Meta:
        db_table = 'evento' # Obriga o banco a chamar a tabela evento e não core_evento como padrao.

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')