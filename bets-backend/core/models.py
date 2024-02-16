from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Bet(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_bets')
    participants = models.ManyToManyField(User, through='BetParticipant', related_name='participated_bets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"[ID:{self.id}]{self.title}"

class BetOption(models.Model):
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE, related_name='options')
    title = models.CharField(null=True, max_length=255)

    def __str__(self):
        return f'"[ID:{self.id}]{self.title}" for [ID:{self.bet.id}]{self.bet.title}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['bet', 'title'], name='unique_betoption_title')
        ]
        unique_together = ('bet', 'title')

class BetParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    chosen_option = models.ForeignKey(BetOption, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'bet')

    def __str__(self):
        return f'{self.user.username} in {self.bet.title}'
