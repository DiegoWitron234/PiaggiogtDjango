from django.db import models

# Create your models here.
class Moto(models.Model):
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='motos/', null=True, blank=True)
    motor = models.CharField(max_length=50)
    velocidad = models.CharField(max_length=50)  # Velocidad máxima en km/h
    manual = models.CharField(max_length=50) 
    pasajeros = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.modelo} ({self.anio})"