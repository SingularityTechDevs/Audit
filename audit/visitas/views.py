from django.shortcuts import render
from django.http import JsonResponse

import json

from datetime import date, timedelta

from django.utils.crypto import get_random_string

from django.contrib.auth.decorators import login_required

from django.utils.dateformat import DateFormat

from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

from datetime import date

from django.core.serializers import serialize

import calendar

import datetime

from core.models import Usuario

from visitas.models import Cita,Visita,MiembroFamilia,Vehiculo,Vivienda,Servicio

from .forms import VisitaForm



def registrar_visita(request):

	print(request)
	

	print(request.POST['arrayfamiliares'])
	print(request.POST['arrayvehiculos'])
	print(request.POST['arrayvivienda'])
	print(request.POST['lat'])
	print(request.POST['long'])
	

	
	lat = request.POST['lat']
	lon = request.POST['long']
	cita = request.POST['cita']

	arrayfamiliares = json.loads(request.POST['arrayfamiliares'])
	arrayvehiculos = json.loads(request.POST['arrayvehiculos'])
	arrayvivienda = json.loads(request.POST['arrayvivienda'])

	print(arrayfamiliares)
	print(arrayvivienda)


	cita_obj = Cita.objects.get(id=cita)
	print(cita_obj)


	visita = Visita.objects.create(inspector=request.user,responsable_visita=request.user,lat=lat,lon=lon,cita=cita_obj)

	
	for x in arrayfamiliares:
		print(x)
		familiar = MiembroFamilia.objects.create(nombres=x[0],apellidos=x[1],parentezco=x[2],ocupacion=x[3],edad=x[4])

		visita.integrantes_familia.add(familiar)

	for x in arrayvehiculos:
		print(x)
		vehiculo = Vehiculo.objects.create(marca=x[0],modelo=x[1],tipo=x[2],año=x[3],modo_adquisicion=x[4],tiempo_con_vehiculo=x[5])

		visita.vehiculos.add(vehiculo)


	for x in arrayvivienda:
		print(x)
		print(x[16])
		vivienda = Vivienda.objects.create(tipo_vivienda=x[0],tipo_techo=x[1],tipo_pared=x[2],direccion=x[3],monto_alquiler=x[4],tiempo_ocupando=x[5],comentario_general=x[6],nevera=x[7],lavadora=x[8],secadora=x[9],luz_contratada=x[10],parabola=x[11],gas=x[12],agua_regular=x[13],telecable=x[14],computadora=x[15],cantidad_computadoras=x[16],cantidad_televisores=x[17],comentarios_televisores=x[18],cantidad_aire_acondicionados=x[19],comentarios_aire_acondicionados=x[20],otros_servicios=x[21],comentario_otros_servicios=x[22],telefono=x[23],comentario_telefono=x[24],comentario_electrodomesticos=x[25])

		visita.vivienda.add(vivienda)

		cita_update = Cita.objects.filter(id=cita).update(estatus="REGISTRADA")

	return JsonResponse("Visita registrada", safe=False)


def eliminar_servicio(request):

	print(request)
	print(request.POST['idservicio'])
	
	idservicio = request.POST['idservicio']

	servicio_obj = Servicio.objects.filter(id=idservicio).delete()


	return JsonResponse("Servicio eliminado", safe=False)

def eliminar_cita(request):

	print(request)
	print(request.POST['idcita'])
	
	idcita = request.POST['idcita']

	cita_obj = Cita.objects.filter(id=idcita).delete()


	return JsonResponse("Cita eliminada", safe=False)

def registrar_cita_new(request):

	print(request)
	print(request.POST['fecha_cita'])
	print(request.POST['tipo_visita'])
	print(request.POST['nombre'])
	print(request.POST['apellido'])
	print(request.POST['identificacion'])
	print(request.POST['sexo'])
	print(request.POST['telefono'])
	print(request.POST['nacimiento'])
	print(request.POST['ciudad_nacimiento'])
	print(request.POST['nacionalidad'])
	print(request.POST['departamento'])
	print(request.POST['puesto'])
	print(request.POST['direccion'])
	print(request.POST['punto_referencia'])
	print(request.POST['estado_civil'])
	print(request.POST['idservicio'])
	


	motivo = request.POST['motivo']
	observaciones = request.POST['observaciones']
	

	fecha_cita = request.POST['fecha_cita']
	tipo_visita = request.POST['tipo_visita']
	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	identificacion = request.POST['identificacion']
	sexo = request.POST['sexo']
	telefono = request.POST['telefono']
	nacimiento = request.POST['nacimiento']
	ciudad_nacimiento = request.POST['ciudad_nacimiento']
	nacionalidad = request.POST['nacionalidad']
	departamento = request.POST['departamento']
	puesto = request.POST['puesto']
	direccion = request.POST['direccion']
	punto_referencia = request.POST['punto_referencia']
	estado_civil = request.POST['estado_civil']
	idservicio = request.POST['idservicio']

	

	servicio_obj = Servicio.objects.get(id=idservicio)
	print(servicio_obj)

	print(fecha_cita)

	datetime_object = datetime.datetime.strptime(fecha_cita, "%Y-%m-%d %I:%M")

	print(datetime_object);


	cita = Cita.objects.create(fecha_visita=datetime_object,tipo_visita=tipo_visita,nombres=nombre,apellidos=apellido,cedula=identificacion,telefonos=telefono,sexo=sexo,fecha_nacimiento=nacimiento,ciudad_nacimiento=ciudad_nacimiento,nacionalidad=nacionalidad,departamento=departamento,puesto=puesto,direccion_residencia=direccion,punto_referencia=punto_referencia,estado_civil=estado_civil,fecha_agendada=fecha_cita,usuario_solicitud=request.user,estatus="PENDIENTE",motivo=motivo,Observaciones=observaciones)

	servicio_obj.visitas.add(cita)




	return JsonResponse("Cita registrada", safe=False)



# Create your views here.
def administrar_citas(request):
	if request.method == 'POST':

		today = datetime.datetime.now()

		month = today.month
		year = today.year
		first, last = calendar.monthrange(year, month)
		print(first, last)

		print(datetime.datetime(year, month, 1))
		print(datetime.datetime(year, month, last))

		inicio_mes = datetime.datetime(year, month, 1)
		fin_mes = datetime.datetime(year, month, last)

		citador = Usuario.objects.get(id=request.user.id)

		td = timedelta(1)



		citas = Cita.objects.filter(usuario_solicitud=request.user)

		citas_data = []
		for cita in citas:
			cita_data = {
				'id': cita.id,
				'usuario_solicitud': cita.usuario_solicitud.username.upper(),
				'fecha_agenda': cita.fecha_agendada.strftime("%Y-%m-%dT%H:%M:%SZ"),
				'fecha_agenda_normal': cita.fecha_agendada,
				'motivo': cita.motivo,
				'obsercaciones': cita.Observaciones
			}
			citas_data.append(cita_data)


		data = {"response":"1","mensaje":"Listado de citas del mes","Citas":citas_data}

		return JsonResponse(data, safe=False)
	
	return render(request, 'citas.html')





def registar_cita(request):

	fecha_cita =  request.POST['fecha_cita']
	motivo = request.POST['motivo']
	observaciones = request.POST['observaciones']
	direccion = request.POST['direccion']

	#fecha_convertida = fecha_cita.strftime(fecha_cita, "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
	date_object = datetime.datetime.strptime(fecha_cita, "%Y-%m-%d %I:%M %p")

	print(date_object)
	#print(fecha_convertida)

	Cita.objects.create(usuario_solicitud=request.user,fecha_agendada=date_object,direccion=direccion,motivo=motivo,Observaciones=observaciones,visitador=request.user,estatus="PENDIENTE")


	data = {"response":"1","mensaje":"Cita creada!"}

	return JsonResponse(data, safe=False)


def administrar_visitas(request):
	if request.method == 'POST':
		form = VisitaForm(request.POST)
		if form.is_valid():
			visita = form.save()
			return JsonResponse({'mensaje': 'Visita creada exitosamente.'})
		else:
			return JsonResponse({'error': 'Error al procesar el formulario.'}, status=400)
	else:
		form = VisitaForm()
	
	return render(request, 'adm_visitas.html', {'form': form})


def consultar_citas(request):

	if request.user.is_superuser:

		citas = Cita.objects.all()

		citas_data = []
		for cita in citas:
			cita_data = {
					'id': cita.id,
					'usuario_solicitud': cita.usuario_solicitud.username.upper(),
					'fecha_agenda': cita.fecha_agendada.strftime('%d/%m/%Y %I:%M %p'),
					'fecha_agenda_normal': cita.fecha_agendada,
					'motivo': cita.motivo,
					'obsercaciones': cita.Observaciones,
					'visitador': cita.visitador.username.upper(),
					'estatus': cita.estatus.upper()

				}
			citas_data.append(cita_data)


		data = {"response":"1","mensaje":"Listado de citas del mes","Citas":citas_data}

		
	else:

		citas = Cita.objects.filter(usuario_solicitud=request.user)

		citas_data = []
		for cita in citas:
			cita_data = {
					'id': cita.id,
					'usuario_solicitud': cita.usuario_solicitud.username.upper(),
					'fecha_agenda': cita.fecha_agendada.strftime('%d/%m/%Y %I:%M %p'),
					'fecha_agenda_normal': cita.fecha_agendada,
					'motivo': cita.motivo,
					'obsercaciones': cita.Observaciones,
					'visitador': cita.visitador.username.upper(),
					'estatus': cita.estatus.upper()
					
				}
			citas_data.append(cita_data)


		data = {"response":"1","mensaje":"Listado de citas del mes","Citas":citas_data}

	return JsonResponse(data, safe=False)

	


def consultar_usuarios(request):

	usuarios = Usuario.objects.all()

	usuarios_data = []
	for usuario in usuarios:
		usuario_data = {
				'id': usuario.id,
				'usuario': usuario.username.upper() + " - " + usuario.first_name + " " + usuario.last_name,
				
			}
		usuarios_data.append(usuario_data)


	data = {"response":"1","mensaje":"Listado de usuarios","Users":usuarios_data}

	return JsonResponse(data, safe=False)

def registrador_visitas(request,id):

	servicio = Servicio.objects.get(id=id)

	return render(request, 'servicio_detail.html',{'servicio':servicio})


def asignar_visitador(request):

	servicio = request.POST['servicio']

	print(servicio)

	idvisitador = request.POST['visitador']

	print(idvisitador)

	visitador = Usuario.objects.get(id=idvisitador)

	print(visitador)

	servicio_obj = Servicio.objects.filter(id=servicio).update(visitador=visitador)


	data = {"response":"1","mensaje":"Nuevo visitador asignado"}

	return JsonResponse(data, safe=False)


def crear_servicio(request):

	servicio_titulo = request.POST['servicio_titulo']

	servicios = Servicio.objects.create(nombre=servicio_titulo.upper(),solcitante=request.user,estatus='PENDIENTE')

	servicios_filter = Servicio.objects.filter(solcitante=request.user)


	servicios_data = []
	for servicio in servicios_filter:
		visitas_asignadas_data = []
		for visita in servicio.visitas.all():
			
			visita_data = {
				'id': visita.id, 
				'nombre': visita.usuario_solicitud.username,
				'nombres': visita.nombres,
				'apellidos': visita.apellidos,
				'fecha': visita.fecha_agendada.strftime('%d/%m/%Y %I:%M %p'),
				'cedula': visita.cedula,
				
			}
			visitas_asignadas_data.append(visita_data)


		servicio_data = {
				'id': servicio.id, 
				'titulo': servicio.nombre,
				'solcitante': servicio.solcitante.username.upper() + " - " + servicio.solcitante.first_name + " " + servicio.solcitante.last_name,
				'fecha': servicio.fecha_solicitud.strftime('%d/%m/%Y %I:%M %p'),
				'visitas': servicio.visitas.count(),
				'visitas_asignadas': visitas_asignadas_data,
		}
		servicios_data.append(servicio_data)


	data = {"servicio":servicios_data,"mensaje":"Nuevo servicio asignado"}

	today = date.today()


	html_body = render_to_string('email_template.html', {
				'usuario_solicitud_username': request.user.username,
				'usuario_solicitud_nombre': request.user.first_name,
				'usuario_solicitud_apellido': request.user.last_name,
				'servicio_nombre': servicios.nombre,
				'fecha':servicios.fecha_solicitud.strftime('%d/%m/%Y %I:%M %p'),
				'fecha2':today.year
				
			})

			
	mail_subject = 'Solicitud nuevo servicio AUDIT'
	text_body = 'Nuevo servicio registrado'
			
	msg = EmailMultiAlternatives(subject=mail_subject, from_email="ceo.singularity@singularity-tech.net",to=[request.user.email], body=text_body)
	msg.attach_alternative(html_body, "text/html")
	msg.send()

	return JsonResponse(data, safe=False)

def detalle_cita_id(request,id):
	cita = Cita.objects.get(id=id)
	return render(request, 'visita.html',{'cita':cita})


def detalle_visita_id(request,id):
	cita = Cita.objects.get(id=id)
	return render(request, 'detalle_visita.html',{'cita':cita})


def consulta_servicio(request):

	servicios_filter = Servicio.objects.filter(solcitante=request.user)


	servicios_data = []
	for servicio in servicios_filter:

		visitas_asignadas_data = []
		for visita in servicio.visitas.all():
			
			visita_data = {
				'id': visita.id, 
				'nombre': visita.usuario_solicitud.username,
				'nombres': visita.nombres,
				'apellidos': visita.apellidos,
				'fecha': visita.fecha_agendada.strftime('%d/%m/%Y %I:%M %p'),
				'cedula': visita.cedula,
				'estatus': visita.estatus,
				
			}
			visitas_asignadas_data.append(visita_data)



		servicio_data = {
				'id': servicio.id, 
				'titulo': servicio.nombre,
				'solcitante': servicio.solcitante.username.upper() + " - " + servicio.solcitante.first_name + " " + servicio.solcitante.last_name,
				'fecha': servicio.fecha_solicitud.strftime('%d/%m/%Y %I:%M %p'),
				'visitas': servicio.visitas.count(),
				'visitador': "SIN ASIGNAR",
				'estatus': servicio.estatus,
				'visitas_asignadas': visitas_asignadas_data,
		}

		

		

		servicios_data.append(servicio_data)


	data = {"servicio":servicios_data,"mensaje":"lista_servicio"}

	return JsonResponse(data, safe=False)



