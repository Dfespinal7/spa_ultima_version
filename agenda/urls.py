from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('contacto', views.contacto, name="contacto"),
    path('', views.inicio, name="inicio"),
    path("iniciosesion", views.login, name="login"),
    path("logout/", views.logout, name="logout"),



    path("registro", views.register, name="register"),
    path('listar_usuario', views.usuario, name="listar_usuario"),
    path('form_usuario', views.form_usuario, name="form_usuario"),
    path('usuario_guardar',views.usuario_guardar,name="usuario_guardar"),
    path('usuario_editar_formulario<int:idUsuario>',views.usuarios_editar_formulario,name="usuario_editar_formulario"),
    path('usuario_eliminar<int:idUsuario>',views.usuarios_eliminar,name="usuario_eliminar"),
    path('buscar_usuario',views.buscar_usuario, name="buscar_usuario"),


    path('agenda', views.agenda, name="agenda"),
    path('listar_citas', views.listar_citas, name="listar_citas"),
    path('form_citas',views.form_citas,name="form_citas"),
    path('guardar_cita',views.guardar_cita,name="guardar_cita"),
    path('editar_cita<int:idCita>',editar_cita,name="editar_cita"),
    path('eliminar_cita<int:idCita>',views.eliminar_cita,name="eliminar_cita"),
    path('buscar_cita',views.buscar_cita, name="buscar_cita"),




    path('servicios',views.servicios,name="servicios"),
    path('listar_servicio',listar_servicios,name="listar_servicio"),
    path('form_servicio',views.form_servicio,name="form_servicio"),
    path('guardar_servicio',views.guardar_servicio,name="guardar_servicio"),
    path('editar_form_servicio<int:idServicio>',views.editar_form_servicio,name="edit_form_servicio"),
    path('eliminar_servicio<int:idServicio>',views.eliminar_Servicio,name="eliminar_servicio"),
    path('buscar_servicio',views.buscar_servicio, name="buscar_servicio"),


    path('empleados',views.empleados,name="empleados"),
    path('listar_empleado',listar_empleado,name="listar_empleado"),
    path('form_empleado',views.form_empledo,name="form_empleado"),
    path('guardar_empleado',views.guardar_empleado,name="guardar_empleado"),
    path('editar_empleado<int:idEmpleado>',views.editar_empleado,name="editar_empleado"),
    path('eliminar_empleado<int:idEmpleado>',views.eliminar_empleado,name="eliminar_empleado"),
    path('buscar_empleados',views.buscar_empleado, name="buscar_empleado"),


    path('listar_pago',listar_pagos,name="listar_pago"),
    path('form_pagos',form_pagos,name="form_pagos"),
    path('guardar_pago',guardar_pagos,name="guardar_pagos"),
    path('editar_pagos<int:idPago>',editar_pagos,name="editar_pagos"),
    path('eliminar_pagos<int:idPago>',eliminar_pago,name="eliminar_pagos"),
    path('buscar_pago',views.buscar_pago, name="buscar_pago"),

    path('ver_mis_citas',views.ver_mis_citas, name="ver_mis_citas"),
    path('form_cita_cliente',views.form_cita_cliente, name="form_cita_cliente"),
    path('guardar_cita_cliente',views.guardar_cita_cliente, name="guardar_cita_cliente"),
    path('ver_perfil',views.ver_perfil, name="ver_perfil"),
    path('cambiar-contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    path('olvidar-contraseña/', views.solicitud_restaurar_contrasena, name='olvidar_contraseña'),
    path('reset-password/<str:token>/', views.reset_password_view, name='reset_password'),



]