from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class Usuario(models.Model):
    ROLES=(
        (1,"Administrador"),
        (2,"Empleado"),
        (3,"Usuario")
    )
    idUsuario=models.BigAutoField(primary_key=True,blank=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    nombreUsuario=models.CharField(max_length=50,unique=True)
    contrasena=models.CharField(max_length=128)  # Cambiado a 128 para almacenar hash seguro
    rol=models.IntegerField(choices=ROLES,default=3)
    password_reset_token = models.CharField(max_length=100, null=True, blank=True)

    def set_password(self, raw_password):
        self.contrasena = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contrasena)
    


    def __str__(self):
        return f"{self.nombre}"








class Servicio(models.Model):
    idServicio=models.BigAutoField(unique=True,primary_key=True)
    nombre=models.CharField(max_length=50)
    duracion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=240)
    precio=models.CharField(max_length=50)
    disponibilidad=models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.nombre}"

class UsuarioServicio(models.Model):
    idUsuarioServicio=models.BigAutoField(primary_key= True,blank=True)
    idUsuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    idServicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)


class Empleado(models.Model):
    idEmpleado=models.BigAutoField(unique=True, primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    cargo=models.CharField(max_length=50)
    salario=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class servicioempleado(models.Model):
    idServicioEmpleado=models.BigAutoField(primary_key=True, blank= True)
    idServicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    idEmpleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)

class Cita(models.Model):
    idCita=models.BigAutoField( primary_key=True, blank=True)
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateField()
    lugar=models.CharField(max_length=50)
    hora=models.TimeField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE,)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,)

    def __str__(self):  
        return f"FECHA: {self.fecha} Y HORA: {self.hora}"
    

class Pago(models.Model):
    idPago=models.BigAutoField(unique=True,primary_key=True)
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaPago=models.DateField()
    monto=models.CharField(max_length=50)
    estadoPago=models.CharField(max_length=50)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    




