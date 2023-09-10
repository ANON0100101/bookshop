from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUser(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookshop', verbose_name='У Марины!')

    def __str__(self):
        return f'{self.title}'


