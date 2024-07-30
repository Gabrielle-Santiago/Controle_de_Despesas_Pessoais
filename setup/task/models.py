from django.db import models

class Renda(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.valor} - {self.data}"
    

class Despesa(models.Model):
    categoria = models.TextField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.categoria} - {self.valor} - {self.data}"
