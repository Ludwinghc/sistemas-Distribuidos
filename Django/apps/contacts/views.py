from django.shortcuts import render, HttpResponse, redirect
from .models import Contact

# Librerias para  enviar correo
from django.core.mail import EmailMessage 
from django.conf import settings
from django.template.loader import render_to_string
# from django.contrib import messages

# Create your views here.
def contactame(request):
  if request.method == 'POST':
    tname = request.POST['name']
    tlast_name = request.POST['last_name']
    temails = request.POST['email']
    tphone = request.POST['phone']
    tmessage = request.POST['message']
    obj_contact = Contact(name=tname,last_name=tlast_name, email=temails, phone=tphone, message=tmessage)
    obj_contact.save()

    # Inicio de codigo para enviar correo
    template_contact = render_to_string('pages/contacts_proof.html',{
      'name': tname,
      'last_name': tlast_name,
      'email': temails,
      'phone': tphone,
      'message': tmessage
    })

    email = EmailMessage(
      tname,
      template_contact,
      settings.EMAIL_HOST_USER,
      ['ludwing2002@gmail.com']
    )

    email.fail_silently = False
    email.send()
    # messages.success(request, 'Se envio el Correo')
    # ? duda para el profe si cambio el render por redirect me aparece un error
    return render(request, '../templates/pages/inicio.html')

  return render(request, 'pages/contacts.html')