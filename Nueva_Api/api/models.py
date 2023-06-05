from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True,null=False)
    dni = models.IntegerField(null=False)
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    telefono = models.CharField(max_length=15,null=False)
    ciudad = models.CharField(max_length=45,null=False)
    usuario = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=100,null=False)
    password = models.CharField(max_length=45,null=False)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
