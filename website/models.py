from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=123, default="João")
    email = models.EmailField(default="default@default.com")
    phone = models.BigIntegerField(default=123456)
    pres_letter = models.TextField(default="Presentation letter")
    linkedin_link = models.URLField(default="http://google.com")
    github_link = models.URLField(default="http://bing.com")
    eng_level = models.IntegerField(default=1)
    salary = models.DecimalField(default=123.45, decimal_places = 2, max_digits = 10)
    curriculum = models.FileField(null=True, blank=True, upload_to='cv_upload')