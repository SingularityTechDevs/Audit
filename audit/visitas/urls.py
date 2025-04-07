from django.urls import path
from .views import administrar_citas,registar_cita,administrar_visitas,registrar_visita,consultar_citas,consultar_usuarios,registrador_visitas,asignar_visitador,crear_servicio,consulta_servicio,registrar_cita_new,eliminar_servicio,eliminar_cita,detalle_cita_id,detalle_visita_id
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('administrar_citas/', administrar_citas, name='administrar_citas'),
    path('registar_cita/', registar_cita, name='registar_cita'),
    path('administrar_visitas/', administrar_visitas, name='administrar_visitas'),
    path('registrar_visita/', registrar_visita, name='registrar_visita'),
    path('consultar_citas/', consultar_citas, name='consultar_citas'),
    path('consultar_usuarios/', consultar_usuarios, name='consultar_usuarios'),
    path('registrador_visitas/<slug:id>/', registrador_visitas, name='registrador_visitas'),
    path('asignar_visitador/', asignar_visitador, name='asignar_visitador'),
    path('crear_servicio/', crear_servicio, name='crear_servicio'),
    path('consulta_servicio/', consulta_servicio, name='consulta_servicio'),
    path('registrar_cita_new/', registrar_cita_new, name='registrar_cita_new'),
    path('eliminar_servicio/', eliminar_servicio, name='eliminar_servicio'),
    path('eliminar_cita/', eliminar_cita, name='eliminar_cita'),
    path('detalle_cita_id/<slug:id>/', detalle_cita_id, name='detalle_cita_id'),
    path('detalle_visita_id/<slug:id>/', detalle_visita_id, name='detalle_visita_id'),
    
]