from django.db import models

class Candidate(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=123)
    email = models.EmailField()
    phone = models.BigIntegerField()
    pres_letter = models.TextField()
    linkedin_link = models.URLField()
    github_link = models.URLField()
    eng_level = models.IntegerField()
    salary = models.DecimalField(decimal_places = 2, max_digits = 10)
    curriculum = models.FileField(null=True, blank=True, upload_to='cv_upload/')
    