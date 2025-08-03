from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]