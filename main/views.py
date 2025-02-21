from django.shortcuts import render
from .models import Moto
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def inicio(request):
    #Página de inicio
    return render(request, 'main/inicio.html')

def vehiculos(request):
    motos = Moto.objects.all()
    return render(request, 'main/vehiculos.html', {'motos': motos})

def empresa(request):
    #Página de empresa
    return render(request, 'main/empresa.html')

def servicios(request):
    #Página de servicios
    return render(request, 'main/servicios.html')


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        empresa = request.POST.get('empresa')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')

        # Crear asunto y cuerpo del mensaje
        subject = f"Consulta de {nombre} - {empresa}"
        message_body = (
            f"Nombre: {nombre}\n"
            f"Empresa: {empresa}\n"
            f"Correo: {email}\n"
            f"Teléfono: {telefono}\n\n"
            f"Mensaje:\n{mensaje}"
        )

        # Define a quién se envía (por ejemplo, al email corporativo)
        recipient_list = ['maximusdiegoalonsodbz@gmail.com']

        try:
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, recipient_list)
            messages.success(request, "Su consulta se ha enviado correctamente.")
        except Exception as e:
            messages.error(request, "Hubo un error al enviar su consulta. Por favor, inténtelo nuevamente.")

        # Redirige a la misma página o a otra de confirmación
        return redirect('contacto')

    return render(request, 'main/contacto.html')