from django.db import models

# Create your models here.


class Accident(models.Model):
    radicado = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    longitud = models.FloatField(null=False,default=0)
    latitud = models.FloatField(null=False,default=0)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"{self.id} {self.radicado} {self.created} {self.longitud} "