from django.db import models

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = 'boardgames'

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'players'

    def __str__(self):
        return self.name
