from django.shortcuts import render, HttpResponse
from .models import Contact

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

  return render(request, 'pages/contacts.html')
