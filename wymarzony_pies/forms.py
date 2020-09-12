import datetime

from django import forms
from django.contrib.auth.models import User
from wymarzony_pies.models import Training, Trainer, Customer, Reservation


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_permissions']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        if data['res_from'] >= data['res_to']:
            raise forms.ValidationError("Błędne godziny rezerwacji!")
        elif data['res_from'] < 0 or data['res_to'] < 0:
            raise forms.ValidationError("Godzina rezerwacji nie może być mniesza od zera!")
        if datetime.date.today() > data['date_of_reservation']:
            raise forms.ValidationError("Błędna data rezerwacji!")

    class Meta:
        model = Reservation
        exclude = ['user']
        widgets = {'date_of_reservation': DateInput(),
                   }


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        widgets = {'description': forms.Textarea()}


class TrainingFrom(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'
        widgets = {'description': forms.Textarea()}



# class TrainingForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         group = Group.objects.get(name='klienci')
#         self.fields['trener'].queryset = group.user_set.all()
#     class Meta:
#         model = Training
#         fields = "__all__"

