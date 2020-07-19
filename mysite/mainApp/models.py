from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class mainApp(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='mainApp',
                               on_delete=models.CASCADE)
