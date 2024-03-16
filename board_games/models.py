from django.db import models

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = 'boardgames'

    def __str__(self):
        return self.name

# lisättävä vielä model loan tai vastaava
