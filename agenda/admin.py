from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display=["idUsuario","nombre","apellido","contacto","email","nombreUsuario","contrasena","rol"]
    search_fields=["idUsuario","nombre"]

class CitasAdmin(admin.ModelAdmin):
    list_display=["idCita","idUsuario","fecha","lugar","hora","servicio","empleado"]
    search_fields=["idcita","servicio"]

class servicioAdmin(admin.ModelAdmin):
    list_display=["idServicio","nombre","duracion","descripcion","precio","disponibilidad"]
    search_fields=["idServicio","nombre"]

class empleadoAdmin(admin.ModelAdmin):
    list_display=["idEmpleado","nombre","apellido","contacto","email","fechaNacimiento","cargo","salario"]
    search_fields=["idEmpleado","nombre"]

class pagosAdmin(admin.ModelAdmin):
    list_display=["idPago","idUsuario","fechaPago","monto","estadoPago",]
    search_fields=["idPago","idUsuario"]




# Register your models here.
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Cita,CitasAdmin)
admin.site.register(Servicio,servicioAdmin)
admin.site.register(Empleado, empleadoAdmin)
admin.site.register(Pago, pagosAdmin)
