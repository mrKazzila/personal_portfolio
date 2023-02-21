from django.db import models


class BlogModel(models.Model):
    title = models.CharField(
        max_length=150,
    )
    description = models.TextField(
        max_length=300,
    )
    date_creation = models.DateField()

    def __str__(self):
        return self.title
