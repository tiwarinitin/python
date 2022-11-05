from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
class Post(models.Model):

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    publish = models.DateTimeField(default=timezone.now)