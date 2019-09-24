from django.shortcuts import render,redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from apps.about.views import getinfo
from django.contrib import messages

class Contact(View):

    def get(self,request,*args, **kwargs):
        form = ContactForm()
        context = {
            'form':form,
            'info':getinfo(),
        }
        return render(request, 'contact/contact.html',context)

    def post(self,request,*args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():         
            ##################################################
            email_nombre = form.cleaned_data.get("name")
            email_from = form.cleaned_data.get("email") 
            email_mensaje = "{}, \n{}".format(email_nombre,form.cleaned_data.get("message"))
            send_mail(
                "MENSAJE DE GNSTORE",#subject
                email_mensaje,
                email_from,
                [settings.EMAIL_HOST_USER ],#email_to
                fail_silently=False
            )
            #################################################
            form.save()
            messages.success(request, 'Your mensaje se envio correctamente.')
            return redirect('contact')#solo poer el name de la url sin extension
        else:
            context = {
                'form':form
            }
            return render(request,'contact/contact.html',contexto)

