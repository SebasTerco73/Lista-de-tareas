from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=20)
    fundacion = models.IntegerField()
    #empleados -> foreignKey -> programador (simulada con el related_name)
    
    # Funciona como un toString
    def __str__(self):
        return self.nombre
    
class Lenguaje(models.Model):
    nombre = models.CharField(max_length=40)
    creador = models.CharField(max_length=40, null=True)
    
    def __str__(self):
        return self.nombre
    
class Programador(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(null=True)
    # Cascada = Si se borra la empresa, se borra el programador
    # related_name: Simula una foreignkey en Empresa vinculando a programador
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="empleados")
    # Relacion Muchos a muchos - Crea una tabla intermedia por atras, no se ve
    lenguaje = models.ManyToManyField(Lenguaje)

    def __str__(self):
        return self.nombre

        

    