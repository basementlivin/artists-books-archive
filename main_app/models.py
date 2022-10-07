from xml.dom.minidom import AttributeList
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    publisher = models.CharField(max_length=150)
    release_year = models.CharField(max_length=4)
    description = models.TextField(max_length=2000)
    image = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]