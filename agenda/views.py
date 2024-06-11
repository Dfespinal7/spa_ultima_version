from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

# Create your views here.



def usuario(request):
    result = Usuario.objects.all()
    context = {"data": result}
    return render(request, 'agenda/usuario/listar_usuario.html', context)


def form_usuario(request):
    return render(request, 'agenda/usuario/form_usuario.html')


def usuario_guardar(request):
    if request.method == 'POST':
        id = request.POST.get("idUsuario")
        nomb = request.POST.get("nombre")
        ape = request.POST.get("apellido")
        cont = request.POST.get("contacto")
        email = request.POST.get("email")
        nomusu = request.POST.get("nombreUsuario")
        contra = request.POST.get("contrasena")
        rol=request.POST.get("rol")
        if id == "":
            # crear
            try:
                q = Usuario(nombre=nomb, apellido=ape, contacto=cont, email=email, nombreUsuario=nomusu,
                            contrasena=contra, rol=rol)
                q.save()
                messages.success(request, "guardado correctamente")
            except Exception as e:
                messages.warning(request, f"error.{e}")

        else:
            # actualizar
            try:
                q = Usuario.objects.get(pk=id)
                q.nombre = nomb
                q.apellido = ape
                q.contacto = cont
                q.email = email
                q.nombreUsuario = nomusu
                q.contrasena = contra
                q.rol=rol
                q.save()
                messages.success(request, "actualizacion correcta")

            except Exception as e:
                messages.error(request, f"error.{e}")
        if "logueo" in request.session and request.session["logueo"]:
            return HttpResponseRedirect(reverse("listar_usuario", args=()))
        else:
            return HttpResponseRedirect(reverse("inicio", args=()))


    else:
        messages.error(request, "no se enviaron datos")
        return HttpResponseRedirect(reverse("form_usuario", args=()))


def usuarios_editar_formulario(request, idUsuario):
    q = Usuario.objects.get(pk=idUsuario)
    contexto = {"id": idUsuario, "data": q}
    return render(request, 'agenda/usuario/form_usuario.html', contexto)


def usuarios_eliminar(request, idUsuario):
    try:
        q = Usuario.objects.get(pk=idUsuario)
        q.delete()
        messages.success(request, "registro eliminado correctamente")
    except Exception as e:
        messages.error(request, f"error: {e}")
    return HttpResponseRedirect(reverse("listar_usuario", args=()))


def agenda(request):
    listar = Cita.objects.all()
    contexto = {"datos": listar}
    return render(request, 'agenda/citas/agenda.html', contexto)


def listar_citas(request):
    
    listar=Cita.objects.all()
    contexto={"datos":listar}
    return render(request,'agenda/citas/listar_cita.html',contexto)


def form_citas(request):
    query = Usuario.objects.all()
    query1=Servicio.objects.all()
    query2=Empleado.objects.all()
    contex = {"usuarios": query,"servicios":query1,"empleados":query2}
    return render(request, 'agenda/citas/form_citas.html', contex)



def guardar_cita(request):
    if request.method=="POST":
        id=request.POST.get("idCita")
        usu=Usuario.objects.get(pk=request.POST.get("usuario"))
        fe=request.POST.get("fecha")
        lu=request.POST.get("lugar")
        hora=request.POST.get("hora")
        ser=Servicio.objects.get(pk=request.POST.get("servicio"))
        emp=Empleado.objects.get(pk=request.POST.get("empleado"))
        
        if id=="":
            try:
                
                ci=Cita(idUsuario=usu,fecha=fe,lugar=lu,hora=hora,servicio=ser,empleado=emp)
                ci.save()
                messages.success(request,"guardado correctamente")
            except Exception as e:
                messages.error(request,f"error:{e}")
            return HttpResponseRedirect(reverse("inicio",args=()))
        else:
            try:
                q=Cita.objects.get(pk=id)
                q.idUsuario=usu
                q.fecha=fe
                q.lugar=lu
                q.hora=hora
                q.servicio=ser
                q.empleado=emp
                q.save()
                messages.error(request,"Actualizado Correctamente")
            except Exception as e:
                messages.error(request,f"error:{e}")
            return HttpResponseRedirect(reverse("listar_citas",args=()))

def editar_cita(request,idCita):
    query=Usuario.objects.all()
    query1=Servicio.objects.all()
    query2=Empleado.objects.all()
    q=Cita.objects.get(pk=idCita)
    context={"id":idCita,"data":q,"usuarios":query,"servicios":query1,"empleados":query2}
    return render(request,'agenda/citas/form_citas.html', context)
  


def eliminar_cita(request, idCita):
    try:
        q = Cita.objects.get(pk=idCita)
        q.delete()
        messages.success(request,'CIta eliminada correctamente')
    except:
        pass
    return HttpResponseRedirect(reverse('inicio', args=()))


def servicios(request):
    result = Servicio.objects.all()
    context = {"datos": result}
    return render(request, 'agenda/servicios/servicios.html', context)

def listar_servicios(request):
    result=Servicio.objects.all()
    context={"datos":result}
    return render(request,'agenda/servicios/listar_servicio.html',context)


def form_servicio(request):
    return render(request, 'agenda/servicios/form_servicio.html')


def guardar_servicio(request):
    if request.method=="POST":
        id=request.POST.get("idServicio")
        nom=request.POST.get("nombre")
        dur=request.POST.get("duracion")
        desc=request.POST.get("descripcion")
        pre=request.POST.get("precio")
        disp=request.POST.get("disponibilidad")
        if id=="":

            try:
                ser=Servicio(nombre=nom,duracion=dur,descripcion=desc,precio=pre,disponibilidad=disp)
                ser.save()
            except:
                pass
            return HttpResponseRedirect(reverse("listar_servicio",args=()))
        else:
            try:
                q=Servicio.objects.get(pk=id)
                q.nombre=nom
                q.duracion=dur
                q.descripcion=desc
                q.precio=pre
                q.disponibilidad=disp
                q.save()
            except:
                pass
            return HttpResponseRedirect(reverse("listar_servicio",args=()))
    else:
        messages.error(request,"no se enviaron datos")
        return HttpResponseRedirect(reverse("form_servicio",args=()))





def editar_form_servicio(request, idServicio):
    q=Servicio.objects.get(pk=idServicio)
    contex={"id":idServicio,"data":q}
    return render(request, 'agenda/servicios/form_servicio.html', contex)

def eliminar_Servicio(request, idServicio):
    try:
        q=Servicio.objects.get(pk=idServicio)
        q.delete()
    except Exception as e:
        messages.error(request,f"error:{e}")
    return HttpResponseRedirect(reverse("listar_servicio",args=()))



def empleados(request):
    result = Empleado.objects.all()
    context = {"data": result}
    return render(request, 'agenda/empleados/empleados.html', context)

def listar_empleado(request):
    result=Empleado.objects.all()
    context={"data":result}
    return render(request, 'agenda/empleados/listar_empleado.html',context)


def form_empledo(request):
    return render(request, 'agenda/empleados/form_empleado.html')


def guardar_empleado(request):
    if request.method == "POST":
        id = request.POST.get("idEmpleado")
        nomb = request.POST.get("nombre")
        ape = request.POST.get("apellido")
        ape = request.POST.get("apellido")
        cont = request.POST.get("contacto")
        email = request.POST.get("email")
        fecha = request.POST.get("fechaNacimiento")
        car = request.POST.get("cargo")
        sala = request.POST.get("salario")
        if id == "":

            try:
                emp = Empleado(nombre=nomb, apellido=ape, contacto=cont, email=email, fechaNacimiento=fecha, cargo=car,
                               salario=sala)
                emp.save()
            except:
                pass
            return HttpResponseRedirect(reverse("listar_empleado", args=()))
        else:
            try:
                q = Empleado.objects.get(pk=id)
                q.nombre = nomb
                q.apellido = ape
                q.contacto = cont
                q.email = email
                q.fechaNacimiento = fecha
                q.cargo = car
                q.salario = sala
                q.save()
            except:
                pass
            return HttpResponseRedirect(reverse("listar_empleado", args=()))
    else:
        messages.error(request, "no se enviaron datos")
        return HttpResponseRedirect(reverse("form_servicio", args=()))


def editar_empleado(request, idEmpleado):
    result = Empleado.objects.get(pk=idEmpleado)
    contex = {"id": idEmpleado, "data": result}
    return render(request, 'agenda/empleados/form_empleado.html', contex)


def eliminar_empleado(request, idEmpleado):
    try:
        q = Empleado.objects.get(pk=idEmpleado)
        q.delete()
    except:
        pass
    return HttpResponseRedirect(reverse("listar_empleado", args=()))


def listar_pagos(request):
    pago=Pago.objects.all()
    contex={"data":pago}
    return render(request, 'agenda/pagos/listar_pago.html',contex)

def form_pagos(request,):
    resut=Usuario.objects.all()
    resulta=Servicio.objects.all()
    context={"usuarios":resut,"servicio":resulta}
    return render(request,'agenda/pagos/form_pagos.html', context)

def guardar_pagos(request):
    if request.method=='POST':
        id=request.POST.get("idPago")
        usu=Usuario.objects.get(pk=request.POST.get("idUsuario"))
        fe=request.POST.get("fechaPago")
        mon=request.POST.get("monto")
        pag=request.POST.get("estadoPago")
        ser=Servicio.objects.get(pk=request.POST.get("servicio"))
        if id=="":
            try:
                
                q=Pago(idUsuario=usu,fechaPago=fe,monto=mon,estadoPago=pag,servicio=ser)
                q.save()
                messages.success(request,"Guardado correctamente!!")
            except Exception as e:
                messages.error(request,f"error:{e}")
            return HttpResponseRedirect(reverse('listar_pago',args=()))
        else:
            try:
                q=Pago.objects.get(pk=id)
                q.idUsuario=usu
                q.fechaPago=fe
                q.monto=mon
                q.estadoPago=pag
                q.servicio=ser
                q.save()
                messages.success(request,"Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"error:{e}")
            return HttpResponseRedirect(reverse('listar_pago',args=()))
    else:
        pass

def editar_pagos(request,idPago):
    resut=Usuario.objects.all()
    resulta=Servicio.objects.all()
    resul=Pago.objects.get(pk=idPago)
    context={"id":idPago,"data":resul,"usuarios":resut,"servicio":resulta}
    return render(request,'agenda/pagos/form_pagos.html',context)

def eliminar_pago(request,idPago):
    try:
        resul=Pago.objects.get(pk=idPago)
        resul.delete()
        messages.success(request,"Pago eliminado!!")
    except Exception as e:
        messages.error(request,f"error:{e}")
    return HttpResponseRedirect(reverse("listar_pago"))


def login(request):
    if request.method == "POST":

        usuario = request.POST.get("nombreUsuario")
        clave = request.POST.get("contrasena")

        try:
            q = Usuario.objects.get(nombreUsuario=usuario, contrasena=clave)
            messages.success(request, "Bienvenido!!")

            datos = {
                "rol": q.rol,
                "nombre": f"{q.nombre} {q.apellido}",
                "id":q.idUsuario,
                "email":q.email,
                "contacto":q.contacto,
                "user":q.nombreUsuario
            }
            print(datos["contacto"])
            request.session["logueo"] = datos
            return HttpResponseRedirect(reverse("inicio"))

        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña no válidos...")
            return render(request, "agenda/login.html")
    else:
        if request.session.get("logueo", False):
            return HttpResponseRedirect(reverse("inicio"))
        else:
            return render(request, "agenda/login.html")
        
def inicio(request):
   
    return render(request, "agenda/inicio.html")


def contacto(request):
    return render(request, 'agenda/contacto/contacto.html')


def register(request):
    return render(request, 'agenda/registro.html')


def logout(request):
	try:
		del request.session["logueo"]
		messages.success(request,"Sesión cerrada correctamente!")
	except Exception as e:
		messages.error(request, f"Error: {e}")
	return HttpResponseRedirect(reverse("login"))


def buscar_usuario(request):
    if request.method=='POST':
        buscar=request.POST.get("buscar")
        query= Usuario.objects.filter(nombre__icontains=buscar)
        

        contex={"data":query,"buscado":buscar}
        return render(request, 'agenda/usuario/listar_usuario.html',contex)
    else:
        messages.warning(request,"No se encontro Usuario")
    return HttpResponseRedirect(reverse("listar_usuario"))


def buscar_cita(request):
    if request.method=='POST':
        cita=request.POST.get("buscarcita")
        query=Cita.objects.filter(idUsuario__nombre__icontains=cita)
        context={"data":cita,"datos":query}
        return render(request,'agenda/citas/listar_cita.html',context)
    else:
        messages.warning(request,"No se encontro Usuario")
    return HttpResponseRedirect(reverse("listar_citas"))







def buscar_pago(request):
    if request.method == 'POST':
            pago = request.POST.get("buscarpago")
        
        
            quer = Pago.objects.filter(idUsuario__nombre__icontains=pago)
            context = {"data": quer, "buscado": pago}
            return render(request, 'agenda/pagos/listar_pago.html', context)
    
def buscar_servicio(request):
    if request.method=='POST':
        buscar=request.POST.get("ser")
        query=Servicio.objects.filter(nombre__icontains=buscar)
        contex={"datos":query,"buscado":buscar}
        
        return render(request,'agenda/servicios/listar_servicio.html',contex)
    return HttpResponseRedirect(reverse("listar_servicio"))
    
        
def buscar_empleado(request):
    if request.method=='POST':
        empleado=request.POST.get("empleado")
        q=Empleado.objects.filter(nombre__icontains=empleado)
        contex={"buscar":empleado,"data":q}
        return render(request,'agenda/empleados/listar_empleado.html',contex)
    return HttpResponseRedirect(reverse("listar_empleado"))
    

        
def ver_mis_citas(request):
    
    # En ver_mis_citas
    usuario = request.session.get("logueo", False)
    q = Usuario.objects.get(pk=usuario["id"])

    cita=Cita.objects.filter(idUsuario=q)
    context={"citas":cita,"data":q}
    return render(request,'agenda/citas/mis_citas.html',context)


def form_cita_cliente(request):
    
    query1=Servicio.objects.all()
    query2=Empleado.objects.all()
    contex = {"servicios":query1,"empleados":query2}
    return render(request,'agenda/citas/form_cita_cliente.html',contex)


def guardar_cita_cliente(request):
    if request.method=="POST":
        usu=request.session["logueo"]
        usu=Usuario.objects.get(pk=usu["id"])
        fe=request.POST.get("fecha")
        lu=request.POST.get("lugar")
        hora=request.POST.get("hora")
        ser=Servicio.objects.get(pk=request.POST.get("servicio"))
        emp=Empleado.objects.get(pk=request.POST.get("empleado"))
        
        try:
                
            ci=Cita(idUsuario=usu,fecha=fe,lugar=lu,hora=hora,servicio=ser,empleado=emp)
            ci.save()
            messages.success(request,"guardado correctamente")
        except Exception as e:
            messages.error(request,f"error:{e}")
        return HttpResponseRedirect(reverse("inicio",args=()))
    
def ver_perfil(request):
    usu=request.session["logueo"]
    return render(request,'agenda/usuario/ver_perfil.html')


def cambiar_contraseña(request):
    if request.method == 'POST':
        nueva_contraseña = request.POST.get('nueva_contraseña')
        usuario_id = request.session.get('logueo', {}).get('id')

        try:
            usuario = Usuario.objects.get(pk=usuario_id)
            usuario.contrasena = nueva_contraseña
            usuario.save()
            messages.success(request, 'Contraseña cambiada exitosamente.')
            return redirect('ver_perfil')  # Redirigir a la página de perfil después de cambiar la contraseña
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')
            return redirect('ver_perfil')  # O redirigir a alguna otra página

    return render(request, 'agenda/usuario/cambiar_contraseña.html')



def solicitud_restaurar_contrasena(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return render(request, 'agenda/solicitud_restaurar_contrasena.html',
                          {'error': 'No se encontró ningún usuario con este correo electrónico.'})

        token = str(uuid.uuid4())
        user.password_reset_token = token
        user.save()

        reset_link = request.build_absolute_uri('/reset-password/') + token

        send_mail(
            'Restablecer contraseña',
            f'Haga clic en el siguiente enlace para restablecer su contraseña: {reset_link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return render(request, 'agenda/usuario/reset_password.html', {'success': True})
    else:
        return render(request, 'agenda/usuario/solicitud_restaurar_contrasena.html')






def reset_password_view(request, token):
    if request.method == 'GET':
        try:
            user = Usuario.objects.get(password_reset_token=token)
        except Usuario.DoesNotExist:
            return render(request, 'agenda/reset_password_invalid.html')  # Crea esta plantilla con el mensaje adecuado

        return render(request, 'agenda/usuario/reset_password_form.html', {'token': token})

    elif request.method == 'POST':
        user = Usuario.objects.get(password_reset_token=token)

        nueva_contraseña = request.POST.get('nueva_contraseña')
        confirmar_contraseña = request.POST.get('confirmar_contraseña')
        if nueva_contraseña == confirmar_contraseña and nueva_contraseña:
            user.contrasena = nueva_contraseña
            user.password_reset_token = None
            user.save()
            return render(request, 'agenda/usuario/reset_password_success.html', {'success': True})  # Enviar 'success' como True
        else:
            return render(request, 'agenda/reset_password_form.html', {'token': token, 'error': 'Las contraseñas no coinciden o son inválidas.'})
