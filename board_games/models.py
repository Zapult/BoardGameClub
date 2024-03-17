from django.db import models
from django.contrib.auth.models import User

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='boardgame_images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'boardgames'

    def __str__(self):
        return self.name

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'loans'

    def __str__(self):
        return self.game
