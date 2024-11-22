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
    cantidad_computadoras = models.PositiveIntegerField(default=0)
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


from django.db import models
from django.contrib.auth.models import User

class Visita(models.Model):
    OPCIONES_TIPO_VISITA = (
        ('Pre-empleo', 'Pre-empleo'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Aleatoria', 'Aleatoria'),
    )

    fecha_visita = models.DateTimeField()
    tipo_visita = models.CharField(max_length=20, choices=OPCIONES_TIPO_VISITA)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefonos = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    ciudad_nacimiento = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    direccion_residencia = models.TextField()
    punto_referencia = models.TextField()
    estado_civil = models.CharField(max_length=20)
    cantidad_dependientes_directos = models.IntegerField()
    integrantes_familia = models.ManyToManyField(MiembroFamilia)
    vehiculos = models.ManyToManyField(Vehiculo)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    monto_alquiler = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tiempo_ocupando = models.CharField(max_length=100, null=True, blank=True)
    inspector = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='visitas_inspeccionadas')
    responsable_visita = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='visitas_asignadas')

    def __str__(self):
        return f"Visita de {self.nombres} {self.apellidos}"
