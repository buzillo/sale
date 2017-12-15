# -*- coding: utf-8 -*-
import smtplib

from django.core.mail import EmailMessage

import mail as mail
from django.shortcuts import render, get_object_or_404

from cars.models import OrderCar, Sta
from cars.forms import OrderFormCar
from sale import settings
from .models import Car, Mail, Scripty, VygodaRapid, VygodaOctavia, VygodaSuperb, VygodaKodiaq, VygodaYeti
from orders.forms import OrderForm, Order_serviceForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from services.models import Service
from django.core import mail
from django.core.mail import get_connection, send_mail, send_mass_mail




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

def rapid(request):
    rapids = VygodaRapid.objects.all()
    return render(request, "cars/vigodas_list.html", {"rapids": rapids})

def octavia(request):
    octavias = VygodaOctavia.objects.all()
    return render(request, "cars/octavia_list.html", {"octavias": octavias})

def superb(request):
    superbs = VygodaSuperb.objects.all()
    return render(request, "cars/superb_list.html", {"superbs": superbs})

def yeti(request):
    yetis = VygodaYeti.objects.all()
    return render(request, "cars/yeti_list.html", {"yetis": yetis})

def kodiaq(request):
    kodiaqs = VygodaKodiaq.objects.all()
    return render(request, "cars/kodiaq_list.html", {"kodiaq": kodiaqs})

def sta(request):
    stas = Sta.objects.all()
    return render(request, "cars/sta.html", {"stas": stas})










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
            servise = int(service)
            usluga = Service.objects.all()[servise].name




            telephone = request.POST.get('phone', '')

            subject = 'Заявка с сайта "Лайфхак SKODA"'
            from_email = settings.EMAIL_HOST_USER

            message = u'''
На сайте "SKODA Лайфхак" появилась новая заявка на услугу! 

Услуга: {0}
Имя клиента: {1} 
Телефон клиента: {2}'''.format(usluga, name, telephone)
            recipient_list = Mail.objects.all()

            messages = [(subject, message, from_email, [recipient]) for recipient in recipient_list]

            send_mass_mail(messages)




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
            form = OrderForm(request.POST)
            name = request.POST.get('name', '')
            carid = request.POST.get('car', '')
            telephone = request.POST.get('phone', '')
            autos = int(carid)
            idauto = Car.objects.all()[autos].idauto
            model = Car.objects.all()[autos].modelcar
            complectation = Car.objects.all()[autos].complectation
            engine = Car.objects.all()[autos].engine
            power = Car.objects.all()[autos].power
            kpp = Car.objects.all()[autos].kpp
            color = Car.objects.all()[autos].color
            oldprice = Car.objects.all()[autos].oldprice
            newprice = Car.objects.all()[autos].newprice



            subject = 'Заявка с сайта "Лайфхак SKODA"'
            from_email = settings.EMAIL_HOST_USER


            message = ''' 
На сайте "SKODA Лайфхак" появилась новая заявка на автомобиль! 
_____________________________________________________________ 

АВТОМОБИЛЬ: 

ID автомобиля: {0} 
ŠKODA {1} {2} | {3}, {4} | {5} | {6}

Цена без скидки: {7} руб.
Цена со скидкой: {8} руб.
_____________________________________________________________

КЛИЕНТ:

Имя клиента: {9} 
Телефон клиента: {10}'''.format(idauto, model, complectation, engine, power, kpp, color, oldprice, newprice, name, telephone)



            recipient_list =  Mail.objects.all()

            messages = [(subject, message, from_email, [recipient]) for recipient in recipient_list]

            send_mass_mail(messages)





            return HttpResponseRedirect(
                "{}?sended=True".format(reverse("car", kwargs={"car_id": car.id})))




    return render(request, "cars/car_detail.html", {
        "car": car,
        "form": form,
        "sended": request.GET.get("sended", False)
    })




def client_adding(request):


        return_dict = dict()

        print(request.POST)
        data = (request.POST)
        name = data.get("name")
        email = data.get("email")
        car = data.get("car")

        autos = int(car)

        idauto = Car.objects.all()[autos].idauto
        model = Car.objects.all()[autos].modelcar
        complectation = Car.objects.all()[autos].complectation
        engine = Car.objects.all()[autos].engine
        power = Car.objects.all()[autos].power
        kpp = Car.objects.all()[autos].kpp
        color = Car.objects.all()[autos].color
        oldprice = Car.objects.all()[autos].oldprice
        newprice = Car.objects.all()[autos].newprice

        OrderCar.objects.create(id_name=name, id_email=email, id_car=car)

        subject = 'Заявка с сайта "Лайфхак SKODA"'
        from_email = settings.EMAIL_HOST_USER

        message = ''' 
        На сайте "SKODA Лайфхак" появилась новая заявка на автомобиль! 
                _____________________________________________________________ 
        
                АВТОМОБИЛЬ: 
            
                ID автомобиля: {0} 
                ŠKODA {1} {2} | {3}, {4} | {5} | {6}
            
                Цена без скидки: {7} руб.
                Цена со скидкой: {8} руб.
                _____________________________________________________________
            
                КЛИЕНТ:
            
                Имя клиента: {9} 
                Телефон клиента: {10}'''.format(idauto, model, complectation, engine, power, kpp, color, oldprice, newprice, name,
                                                email)

        recipient_list = Mail.objects.all()

        messages = [(subject, message, from_email, [recipient]) for recipient in recipient_list]

        send_mass_mail(messages)


        return JsonResponse(return_dict)





