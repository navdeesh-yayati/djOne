from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
