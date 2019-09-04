from django.db import models
import uuid
import os

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('cv_upload/', filename)

class Candidate(models.Model):
    ENG_LEVEL_CHOICES = [
        ('1','Iniciante'),
        ('2','Intermediário'),
        ('3','Avançado'),
        ('4','Nativo'),
    ]
    datetime = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=123)
    email = models.EmailField()
    phone = models.BigIntegerField()
    pres_letter = models.TextField(blank=True)
    linkedin_link = models.URLField()
    github_link = models.URLField()
    eng_level = models.CharField(max_length=16, choices=ENG_LEVEL_CHOICES)
    salary = models.DecimalField(decimal_places = 2, max_digits = 10)
    curriculum = models.FileField(upload_to=upload_path, null=True)
    