from django.db import models

class CovidData(models.Model):
    patient_no = models.IntegerField()
    date = models.TextField()
    # date = models.DateTimeField()
    city = models.TextField()
    state = models.TextField()
