from django.db import models

# Create your models here.
class Shipments(models.Model):
    slno=models.IntegerField()
    destination=models.CharField(max_length=30)
    weight=models.IntegerField()


class DPA(models.Model):
    subsetno=models.IntegerField()
    vertexno=models.IntegerField()
    cost=models.IntegerField()

class DPB(models.Model):
    subsetno=models.IntegerField()
    cost=models.IntegerField()
    slno=models.IntegerField()
