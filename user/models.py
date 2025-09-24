from django.db import models
from core.base_model import BaseModel

class User(BaseModel):
    # Campos base de usúario
    username = models.CharField(max_length=18, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=150, blank=True, null=True)

    # flags de permissão
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Book(BaseModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
