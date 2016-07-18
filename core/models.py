from django.db import models
# Create your models here.

class Substance(models.Model):
    name = models.CharField(max_length=250)
    density = models.IntegerField()

    def __unicode__(self):
        return self.name

