from django.db import models


class Author(models.Model):
    nickname = models.CharField(max_length=100)
    start_carrier = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nickname


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='books')
    length = models.IntegerField()
    published = models.DateField()

    def __str__(self):
        return self.title
