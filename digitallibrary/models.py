from django.db import models
import datetime
# Create your models here.
class publication_types(models.Model):
    name = models.TextField()
    def __str__ (self):
        return(self.name)

class publications(models.Model):
    theme_choice = (
        ("Report","Report"),
        ("Consultancy Files","Consultancy Files"),
        ("Research","Research"),
        ("Plans and Policies","Plans and Policies")
    )
    pub_type_choice =(
        ("Files","Files"),
        ("Audio","Audion"),
        ("Video","Video")
    )
    lang_choices = (
        ("Nepali","Nepali"),
        ("English","English")
    )
    title = models.TextField()
    theme = models.CharField(max_length=200,choices = theme_choice)
    publication_type = models.CharField(max_length=200,choices = pub_type_choice)
    description = models.TextField(blank = True)
    cover_picture = models.ImageField(upload_to = "Pictures/")
    author = models.CharField(max_length=200)
    file = models.FileField()
    file_link = models.URLField()
    published_date = models.DateTimeField(null = True)
    language = models.CharField(max_length=100,choices = lang_choices)