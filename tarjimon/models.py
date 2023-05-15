from django.db import models

class Lugat(models.Model):

    inglizcha = models.CharField('Inglizcha', max_length=128)
    uzbekcha = models.CharField('Uzbekcha', max_length=128)

    def __str__(self):
        return f'{self.inglizcha} {self.uzbekcha}'


class Dictio(models.Model):
    text = models.TextField(blank=False, null=False)
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text