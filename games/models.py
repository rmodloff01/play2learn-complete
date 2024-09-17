from django.db import models

class GameScore(models.Model):

    MATH = "MATH"
    ANAGRAM = "ANAGRAM"

    GAME_CHOICES = [
        (MATH, "Math Facts"),
        (ANAGRAM, "Anagram Hunt")
    ]

    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=ANAGRAM)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    operation = models.TextField()
    max_number = models.TextField()
    word_length = models.TextField()