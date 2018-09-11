import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Comentario(models.Model):
    mensaje = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date publihsed')
    IP_cliente = models.CharField(max_length=200)

    def __str__(self):
        return self.mensaje

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
