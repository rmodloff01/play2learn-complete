from django.db import models
from django.urls import reverse
from django.conf import settings

class Review(models.Model):
    review = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )

    def get_absolute_url(self):
        return reverse('reviews:detail', args=[str(self.pk)])
    
    def __str__(self):
        return self.review