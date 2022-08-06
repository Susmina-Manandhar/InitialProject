from django.db import models

# Create your models here.
class Project(models.Model):
    proj_type = (
        ("Administrative","Administrative"),
        ("Development","Development")
    )
    title = models.TextField()
    title_ne = models.TextField(blank=True)
    type = models.CharField(max_length=200,choices=proj_type)
    