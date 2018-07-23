from django.db import models

class CoNLLU(models.Model):
    head=models.CharField(max_length=200)
    sense=models.CharField(max_length=200)
    rel=models.CharField(max_length=200)
    dep=models.CharField(max_length=200)
    words=models.CharField(max_length=200)
    def __str__(self):
        return vars(self).__str__()
