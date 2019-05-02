from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(Author, models.PROTECT)

    def __str__(self):
        return self.name