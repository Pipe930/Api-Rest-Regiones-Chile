from django.db import models

class Region(models.Model):
    id_region = models.BigAutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    poblacion = models.PositiveIntegerField()
    superficie = models.DecimalField(max_digits=7, decimal_places=1)
    capital = models.CharField(max_length=40, unique=True)
    numero_region = models.CharField(max_length=8, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:

        db_table = "regiones"
        verbose_name = 'region'
        verbose_name_plural = 'regiones'
        ordering = ('nombre',)

class Provincia(models.Model):
    id_provincia = models.BigAutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:

        db_table = "provincias"
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'
        ordering = ('nombre',)
    
class Comuna(models.Model):
    id_comuna = models.BigAutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:

        db_table = "comunas"
        verbose_name = "comuna"
        verbose_name_plural = "comunas"
        ordering = ('nombre',)