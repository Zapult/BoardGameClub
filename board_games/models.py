from django.db import models

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.name
