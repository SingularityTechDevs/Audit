# Audit Django

Este es un proyecto Django configurado para su despliegue automático en **Vercel** usando **GitHub Actions**.

## Requisitos

- Python 3.12 o superior
- Pip
- Git
- Cuenta en **Vercel** y **GitHub**

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/SingularityTechDevs/Audit.git
cd Audit
```

### Instalar dependencias
El archivo requirements.txt contiene todas las dependencias necesarias para ejecutar el proyecto. Para instalar todas las dependencias:

```bash
pip install -r requirements.txt
```
Este comando descargará e instalará las bibliotecas necesarias desde PyPI.

### Configuración de la base de datos

Asegúrate de tener configurada la base de datos en tu entorno local. Luego, ejecuta las migraciones para preparar la base de datos:

```bash
python manage.py migrate
```

## Comandos de Desarrollo

### Para iniciar el servidor local:

```bash
python manage.py runserver
```
Este comando arrancará el servidor de desarrollo de Django y podrás acceder a la aplicación en [http://127.0.0.1:8000/].

### Para ejecutar las pruebas:

```bash
python manage.py test
```
