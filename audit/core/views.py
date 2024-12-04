from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate,login as Login_process,logout
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth import authenticate,login as Login_process,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):

	return render(request, 'index.html')


# Create your views here.
def login(request):
	if request.user.is_authenticated:
		return redirect("index")
	else:
		return render(request, 'login.html',{})
    
	
@login_required
def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/login')



def loginaction(request):
	#Acciones para el Login
	print("PRINT JSON")
	print(request.body)
	data3 = json.loads(request.body)
	print(json.loads(request.body))
	usuario = authenticate(username=data3["username"],password=data3["password"])
	print(usuario)
	if usuario != None:
		if usuario.is_active == True:
			Login_process(request,usuario)
			print("usaurio activo")
			print(usuario)
			print(usuario.username)
			#user = Token.objects.get(user=usuario)
			#print(user)
			#print(user.key)
			responsejson = {"estatus":"OK", "userid":usuario.id,"message":"Sesion Iniciada correctamente"}
			return HttpResponse(json.dumps(responsejson), content_type='application/json')
		else:
			responsejson = {"estatus":"ERROR","message":"Usuario Inactivo"}
			return HttpResponse(json.dumps(responsejson), content_type='application/json')
	else:
		responsejson = {"estatus":"ERROR","message":"Credenciales no son validas, o no existen"}
		return HttpResponse(json.dumps(responsejson), content_type='application/json')