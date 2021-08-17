from django.db import models


class Produto(models.Model):
    nome = models.CharField('Produto', max_length=100)
    preco = models.DecimalField('preço', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome
