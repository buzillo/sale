from django import forms

from cars.models import OrderCar


class OrderFormCar(forms.ModelForm):



    class Meta:
        model = OrderCar
        fields = ["id_name", "id_email", "id_car"]


        widgets = {
            'id_car': forms.TextInput(
                attrs={'placeholder': u'Иванов Иван', 'class': 'col-md-6 col-lg-6 col-xs-6  form-control'}),
            'id_name': forms.TextInput(attrs={'placeholder': u'Иванов Иван', 'class': 'col-md-6 col-lg-6 col-xs-6  form-control'}),
            'id_email': forms.TextInput(attrs={'placeholder': '+ 7 (911) 123-45-67', 'class': 'col-md-6 col-lg-6 col-xs-6 form-control'}),
                }



