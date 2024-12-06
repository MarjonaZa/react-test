from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat=models.ForeignKey('Categoty', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Categoty(models.Model):
    name = models.CharField(max_length=255, db_index=True) #выяснить что такое db_inedx

    def __str__(self):
        return self.name

