from django.contrib.auth.models import User
from django.db import models
import datetime

from django.urls import reverse


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=128, verbose_name='Twoje imię')
    pet_name = models.CharField(max_length=128, verbose_name='Imię psa')
    address = models.CharField(max_length=256, verbose_name='Twój adres')

    def __str__(self):
        return f'Klient {self.customer_name}i pies {self.pet_name}'


class Trainer(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.name}, {self.description}'

    def get_delete_url(self):
        return reverse('del_trainer', args=(self.pk,))


class Location(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    open_form = models.CharField(max_length=128)
    open_to = models.CharField(max_length=128)
    def __str__(self):
        return f'Nazwa szkoły: {self.name}, opis lokalizacji: {self.address}' \
               f', otwarta od {self.open_form} do {self.open_to}'

    def get_delete_url(self):
        return reverse('del_loc', args=(self.pk,))


class Training(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return f'Nazwa szkolenia: {self.name}, opis: {self.description}'

    def get_delete_url(self):
        return reverse('del_training', args=(self.pk,))


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Twój trener')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Rodzaj szkolenia')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Wybierz szkołę')
    date_of_reservation = models.DateField(default=datetime.date.today, verbose_name='Data szkolenia')
    res_from = models.IntegerField(verbose_name='Rezerwacja od')
    res_to = models.IntegerField(verbose_name='Rezerwacja do')

    def __str__(self):
        return f"{self.user} {self.trainer} {self.training}\
             {self.location} {self.date_of_reservation} od {self.res_from}:00 do {self.res_to}:00"

    def get_delete_url(self):
        return reverse('del_res', args=(self.pk,))

    def delete_res(self):
        return reverse('all_res_del', args=(self.pk,))

    def get_detail_url(self):
        return reverse('edit_res', args=(self.pk,))
