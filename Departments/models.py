from django.db import models

# Create your models here.
class department ():
    name = models.TextField(),
    name_ne =models.TextField(blank=True)
    descrip = models.TextField("Description",blank = True)
    