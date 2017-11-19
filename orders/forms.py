# -*- coding: utf-8 -*-
from django import forms
from .models import Order, Order_service
from cars.models import Car
from services.models import Service

class OrderForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Car.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ["car", "name", "phone"]


        widgets = {
            'name': forms.TextInput(attrs={'placeholder': u'Иванов Иван', 'class': 'col-md-6 col-lg-6 col-xs-6  form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '+ 7 (911) 123-45-67', 'class': 'col-md-6 col-lg-6 col-xs-6 form-control'}),
                }


class Order_serviceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order_service
        fields = ["service", "name", "phone"]


        widgets = {
            'name': forms.TextInput(attrs={'placeholder': u'Иванов Иван', 'class': 'col-md-6 col-lg-6 col-xs-6  form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '+ 7 (911) 123-45-67', 'class': 'col-md-6 col-lg-6 col-xs-6 form-control'}),
                }


