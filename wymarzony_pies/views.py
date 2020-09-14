from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from wymarzony_pies.forms import UserForm, TrainerForm, CustomerForm, TrainingFrom, ReservationForm
from wymarzony_pies.models import Location, Trainer, Training, Reservation


class CustomerCreateView(CreateView):
    form_class = CustomerForm
    success_url = reverse_lazy('main_page')
    template_name = 'detail_view.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 'You already have registered a Client with this name. ' + \
                                 'All of your Client names must be unique.')
        return render(request, 'detail_view.html', context=self.get_context_data())

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super(CustomerCreateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs['user_id'] = self.request.user.id
    #     return kwargs


class AddLocation(PermissionRequiredMixin, View):
    permission_required = ['wymarzony_pies.add_location']

    def get(self, request):
        locations = Location.objects.all()
        hours = [item for item in range(6, 22)]
        loc = Location.objects.all()
        return render(request, 'add_location.html', {'loc': loc, 'hours': hours, 'objects': locations})

    def post(self, request):
        hours = [item for item in range(6, 22)]
        name = request.POST['name']
        address = request.POST['description']
        open_from = request.POST.get('open_from')
        open_to = request.POST.get('open_to')
        locations = Location.objects.all()
        if name == "" or address == "" or open_from == "" or open_to == "":
            error_message = 'Uzupełnij wszystie pola!'
            return render(request, 'add_location.html', {'error_message': error_message,
                                                         'objects': locations, 'hours': hours})
        if open_from <= open_to:
            error_message = 'Błędne godziny!'
            return render(request, 'add_location.html', {'error_message': error_message,
                                                         'objects': locations, 'hours': hours})
        Location.objects.create(name=name, address=address, open_form=open_from, open_to=open_to)
        succes_message = 'Szkoła dodana!'
        return render(request,'add_location.html',
                      {'succes_message': succes_message, 'objects': locations})


class LocationDeleteView(View):
    def get(self, request, pk):
        return render(request, 'delete_objects.html', {'obj': Location.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST['delete'] == 'TAK':
            Location.objects.get(pk=pk).delete()
        return redirect(reverse('Location'))


class CreateTrainer(PermissionRequiredMixin, CreateView):
    permission_required = ['wymarzony_pies.add_trainer']
    model = Trainer
    form_class = TrainerForm
    template_name = 'detail_view.html'
    success_url = reverse_lazy('add_trainer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Trainer.objects.all()})
        return context


class TrainerDeleteView(View):
    def get(self, request, pk):
        return render(request, 'delete_objects.html', {'obj': Trainer.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST['delete'] == 'TAK':
            Trainer.objects.get(pk=pk).delete()
        return redirect(reverse('add_trainer'))


class CreateTraining(PermissionRequiredMixin, CreateView):
    permission_required = ['wymarzony_pies.add_training']
    model = Training
    form_class = TrainingFrom
    template_name = 'detail_view.html'
    success_url = reverse_lazy('add_training')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Training.objects.all()})
        return context


class TrainingView(View):
    def get(self, request):
        trainings = Training.objects.all()
        return render(request, 'all_trainings.html', {'objects': trainings})


class TrainingDeleteView(View):
    def get(self, request, pk):
        return render(request, 'delete_objects.html', {'obj': Training.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST['delete'] == 'TAK':
            Training.objects.get(pk=pk).delete()
        return redirect(reverse('add_training'))


class ReservationCreateView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if pk is None:
            form = ReservationForm()
        else:
            value = Reservation.objects.get(pk=pk)
            form = ReservationForm(instance=value)
        return render(request, 'detail_view.html', {'form': form})

    def post(self, request, pk = None):
        if pk is None:
            form = ReservationForm(request.POST)
        else:
            value = Reservation.objects.get(pk=pk)
            form = ReservationForm(request.POST, instance=value)
        if form.is_valid():
            reservation = form.save(commit=False)
            if not hasattr(reservation, 'user'):
                reservation.user = request.user
            reservation.save()
            return redirect(reverse('reservations'))
        return render(request, 'detail_view.html', {'form': form})


class ReservationView(LoginRequiredMixin, View):
    def get(self, request):
        reservation = Reservation.objects.filter(user=request.user)
        if not Reservation.objects.filter(user=request.user):
            message = 'Brak rezerwacji!'
            return render(request, 'obj_list.html', {'message': message})
        return render(request, 'obj_list.html', {'objects': reservation})


class ReservationDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return render(request, 'delete_objects.html', {'obj': Reservation.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST['delete'] == 'TAK':
            Reservation.objects.get(pk=pk).delete()
        return redirect(reverse('reservations'))


class AllReservationView(PermissionRequiredMixin, View):
    permission_required = ['wymarzony_pies.view_reservation']

    def get(self, request):
        all_reservations = Reservation.objects.all()
        form = ReservationForm()
        return render(request, 'res_list.html', {'form': form, 'objects': all_reservations})


class AllReservationDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return render(request, 'delete_objects.html', {'obj': Reservation.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST['delete'] == 'TAK':
            Reservation.objects.get(pk=pk).delete()
        elif request.POST['delete'] == 'NIE':
            redirect('all_res')
        return redirect(reverse('all_res'))



class RegisterView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'detail_view.html'
    success_url = reverse_lazy('login')


class UserChangePermission(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'detail_view.html'

    def get_success_url(self):
        return reverse_lazy("user_permission", args=(self.object.id,))
