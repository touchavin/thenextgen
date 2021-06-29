from django.db import models

# Create your models here.


class netxgen(models.Model):
    Customer = models.CharField(max_length=100, blank=True, null=True)
    