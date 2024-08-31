from django.db import models

# Create your models here.

class Clube(models.Model):
    nome = models.CharField(max_length=50)
    AnoDeFundacao = models.DateField()
    vitorias = models.IntegerField()
    titulos = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Jogadores(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)
    posicao = models.CharField(max_length=100)
    clube_atual = models.TextField()

    def __str__(self):
        return self.nome


#nome: String, nome completo do jogador. data_nascimento: Date, data de nascimento do jogador.nacionalidade: String, país de origem do jogador.posicao: String, posição em campo (por exemplo, "Atacante", "Meia", "Zagueiro").
