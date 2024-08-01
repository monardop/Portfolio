from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from django.forms import DateField


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)

class Certifications(models.Model):
    title = CharField(max_length=250)
    institution = CharField(max_length=250)
    start_date = CharField(max_length=8)
    end_date = CharField(max_length=8)
    description = CharField(max_length=250)

class Experience(models.Model):
    title = CharField(max_length=250)
    company = CharField(max_length=250)
    start_date = CharField(max_length=8)
    end_date = CharField(max_length=8)
    description = CharField(max_length=250)