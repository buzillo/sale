# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Car, Mail, Scripty
from orders.forms import OrderForm, Order_serviceForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from services.models import Service



def cars_list(request):
    try:
        scripts = Scripty.objects.all()
        cars = Car.objects.all()
        raps = Car.objects.filter(modelcar="Rapid")
        yetis = Car.objects.filter(modelcar="Yeti")
        octs = Car.objects.filter(modelcar="Octavia")
        superbs = Car.objects.filter(modelcar="Superb")
        kodiaqs = Car.objects.filter(modelcar="Kodiaq")
        return render(request, "cars/cars_list.html", {
            "cars": cars,
            "raps": raps,
            "yetis": yetis,
            "octs": octs,
            "superbs": superbs,
            "kodiaqs": kodiaqs,
            "scripts": scripts
        })
    except:
        return render(request, "404.html")




def services_list(request):
    try:
        services = Service.objects.all()
        return render(request, "services/services_list.html", {"services": services})
    except:
        return render(request, "404.html")



def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    form = Order_serviceForm(request.POST or None, initial={
        "service": service

    })

    if request.method == "POST":
        if form.is_valid():
            form.save()

            form = Order_serviceForm(request.POST)
            name = request.POST.get('name', '')
            service = request.POST.get('service', '')
            telephone = request.POST.get('phone', '')

            subject = u"Заявка с сайта ЛАЙФХАК SKODA"
            message = u'''
                        На сайте "SKODA Лайфхак" появилась новая заявка на услугу! 

                        Услуга: {1}
                        Имя клиента: {0} 
                        Телефон клиента: {2}'''.format(name, service, telephone)
            sender = 'skoda.sigmaservice@gmail.com'

            mail = Mail.objects.all()
            recipients = [mail]

            send_mail(subject, message, sender, recipients)


            return HttpResponseRedirect(
                "{}?sended=True".format(reverse('service', kwargs={"service_id": service_id})))


    return render(request, "services/service_detail.html", {
        "service": service,
        "form": form,
        "sended": request.GET.get("sended", False)
    })



def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    form = OrderForm(request.POST or None, initial={
        "car": car
    })


    if request.method == "POST":
        if form.is_valid():
            form.save()


            form = OrderForm(request.POST)
            name = request.POST.get('name', '')
            carid = request.POST.get('car', '')
            telephone = request.POST.get('phone', '')

            subject = u"Заявка с сайта ЛАЙФХАК SKODA"
            message = u'''
            На сайте "SKODA Лайфхак" появилась новая заявка на звонок! 
            
            ID машины: {1}
            Имя клиента: {0} 
            Телефон клиента: {2}'''.format(name, carid, telephone)
            sender = 'skoda.sigmaservice@gmail.com'
            mail = Mail.objects.all()

            recipients = [mail]

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect(
                "{}?sended=True".format(reverse("car", kwargs={"car_id": car.id})))


    return render(request, "cars/car_detail.html", {
        "car": car,
        "form": form,
        "sended": request.GET.get("sended", False)
    })
