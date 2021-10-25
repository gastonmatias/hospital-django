from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=25)
    apellido = models.CharField('Apellido',max_length=25)
    rut = models.CharField('Rut (Sin puntos, con guión)',max_length=12)
    fecha_nacimiento = models.DateField('Fecha Nacimiento',null='true',blank=True)
    nacionalidad = models.CharField('Nacionalidad',max_length=25,null='true',blank=True)
    descripcion = models.CharField('Descripcion',max_length=25,null='true',blank=True)
    nickname = models.CharField('Nickname',max_length=10,null='true',blank=True)
    email = models.EmailField('Correo electronico')
    password = models.CharField('Contraseña',max_length = 15)
    telefono = models.CharField('Telefono',max_length = 15)
    celular = models.CharField('Celular',max_length = 15)
    archivo = models.IntegerField('Archivo',null='true',blank=True)
    estado = models.CharField('Estado',max_length=50,null='true',blank=True)
    foto = models.ImageField('Fotografia (Opcional)',upload_to='fotos',null=True, blank='True')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
