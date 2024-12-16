from django.db import models

# Create your models here.
from django.db import models
from core.models import Usuario
# Create your models here.





class PosiblesRiesgos(models.Model):
    violencia_intrafamiliar = models.BooleanField(default=False)
    adicciones = models.BooleanField(default=False)
    otros = models.BooleanField(default=False)
    comentario_otros = models.TextField(blank=True)
    narcotrafico = models.BooleanField(default=False)
    contaminacion = models.BooleanField(default=False)
    vandalismo = models.BooleanField(default=False)
    deslizamiento_tierra = models.BooleanField(default=False)
    delincuencia_visible = models.BooleanField(default=False)
    proximo_canada_rio = models.BooleanField(default=False)
    
    # Otros campos relacionados con los riesgos

    def __str__(self):
        return "Posibles Riesgos"

class Vivienda(models.Model):
    OPCIONES_TIPO_TECHO = (
        ('Techo Zinc', 'Techo Zinc'),
        ('Techo Concreto', 'Techo Concreto'),
    )

    OPCIONES_TIPO_PARED = (
        ('Pared Madera', 'Pared Madera'),
        ('Pared Blocks', 'Pared Blocks'),
    )

    OPCIONES_TIPO_VIVIENDA = (
        ('Propia', 'Propia'),
        ('Alquilada', 'Alquilada'),
    )

    tipo_vivienda = models.CharField(max_length=20, choices=OPCIONES_TIPO_VIVIENDA)
    tipo_techo = models.CharField(max_length=20, choices=OPCIONES_TIPO_TECHO)
    tipo_pared = models.CharField(max_length=20, choices=OPCIONES_TIPO_PARED)
    direccion = models.TextField()
    monto_alquiler = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tiempo_ocupando = models.CharField(max_length=100, null=True, blank=True)
    comentario_general = models.TextField(blank=True)
    nevera = models.BooleanField(default=False)
    cantidad_televisores = models.PositiveIntegerField(default=0)
    comentarios_televisores = models.TextField(blank=True)
    lavadora = models.BooleanField(default=False)
    cantidad_aire_acondicionados = models.PositiveIntegerField(default=0)
    comentarios_aire_acondicionados = models.TextField(blank=True)
    secadora = models.BooleanField(default=False)
    computadora = models.BooleanField(default=False)
    cantidad_computadoras = models.PositiveIntegerField(default=0,blank=True)
    comentario_electrodomesticos = models.TextField(blank=True)
    agua_regular = models.BooleanField(default=False)
    telecable = models.BooleanField(default=False)
    telefono = models.BooleanField(default=False)
    comentario_telefono = models.TextField(blank=True)
    luz_contratada = models.BooleanField(default=False)
    parabola = models.BooleanField(default=False)
    otros_servicios = models.BooleanField(default=False)
    comentario_otros_servicios = models.TextField(blank=True)
    gas = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    # Otros campos relacionados con la vivienda

    def __str__(self):
        return self.direccion

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    modo_adquisicion = models.CharField(max_length=100)
    tiempo_con_vehiculo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class MiembroFamilia(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    parentezco = models.CharField(max_length=100)  # Ejemplo: Padre, Madre, Hijo, Hija, etc.
    edad = models.PositiveIntegerField()
    ocupacion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Cita(models.Model):
    OPCIONES_TIPO_VISITA = (
        ('Pre-empleo', 'Pre-empleo'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Aleatoria', 'Aleatoria'),
    )
    usuario_solicitud = models.ForeignKey(Usuario,related_name='usuario_solicitud', on_delete=models.CASCADE)
    visitador = models.ForeignKey(Usuario, related_name='visitador',on_delete=models.CASCADE,blank=True,
        null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_agendada = models.DateTimeField()
    motivo = models.TextField()
    Observaciones = models.TextField()
    estatus = models.CharField(max_length=200)
    fecha_visita = models.DateTimeField(blank=True)
    tipo_visita = models.CharField(max_length=20, choices=OPCIONES_TIPO_VISITA)
    nombres = models.CharField(max_length=100,null=True, blank=True)
    apellidos = models.CharField(max_length=100,null=True, blank=True)
    cedula = models.CharField(max_length=20,null=True, blank=True)
    telefonos = models.CharField(max_length=20,null=True, blank=True)
    sexo = models.CharField(max_length=10,null=True, blank=True)
    fecha_nacimiento = models.DateField()
    ciudad_nacimiento = models.CharField(max_length=100,null=True, blank=True)
    nacionalidad = models.CharField(max_length=100,null=True, blank=True)
    departamento = models.CharField(max_length=100,null=True, blank=True)
    puesto = models.CharField(max_length=100,null=True, blank=True)
    direccion_residencia = models.TextField()
    punto_referencia = models.TextField()
    estado_civil = models.CharField(max_length=20)


    def __str__(self):
        return f"Cita para {self.usuario_solicitud.first_name} el {self.fecha_agendada}"


from django.db import models
from django.contrib.auth.models import User


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    visitas = models.ManyToManyField(Cita, null=True, blank=True)
    solcitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitante')
    estatus = models.CharField(max_length=100,null=True, blank=True)
    visitador = models.ForeignKey(Usuario, related_name='visitador_servicio',on_delete=models.CASCADE,blank=True,
        null=True)
    

    def __str__(self):
        return f"{self.nombre} - {self.id}"

class Visita(models.Model):
    OPCIONES_TIPO_VISITA = (
        ('Pre-empleo', 'Pre-empleo'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Aleatoria', 'Aleatoria'),
    )
    
    integrantes_familia = models.ManyToManyField(MiembroFamilia, null=True, blank=True)
    vehiculos = models.ManyToManyField(Vehiculo, null=True, blank=True)
    vivienda = models.ManyToManyField(Vivienda, null=True, blank=True)
    inspector = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='visitas_inspeccionadas')
    responsable_visita = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='visitas_asignadas')
    lat = models.CharField(max_length=50,null=True, blank=True)
    lon = models.CharField(max_length=50,null=True, blank=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='cita_visita')
    fecha_registro = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Visita de {self.responsable_visita.username}"


