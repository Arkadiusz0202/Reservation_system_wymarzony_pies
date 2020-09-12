"""Wymarzony_pies_szkolenia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from wymarzony_pies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('user/<int:pk>/', views.UserChangePermission.as_view(), name='user_permission'),
    path('', TemplateView.as_view(template_name='layout.html'), name='main_page'),
    path('customer/', views.CustomerCreateView.as_view(), name='create_customer'),

    path('addloc/', views.AddLocation.as_view(), name='Location'),
    path('addloc/delete/<int:pk>', views.LocationDeleteView.as_view(), name='del_loc'),

    path('addtrainer/', views.CreateTrainer.as_view(), name='add_trainer'),
    path('delatetrainer/<int:pk>', views.TrainerDeleteView.as_view(), name='del_trainer'),

    path('addtraining/', views.CreateTraining.as_view(), name='add_training'),
    path('trainings/', views.TrainingView.as_view(), name='all_trainings'),
    path('deletetraining/<int:pk>', views.TrainingDeleteView.as_view(), name='del_training'),

    path('addreservation/', views.ReservationCreateView.as_view(),name='add_reservation'),
    path('yourreservations/', views.ReservationView.as_view(), name='reservations'),
    path('allreservations/', views.AllReservationView.as_view(), name='all_res'),
    path('allreservations/del/<int:pk>', views.AllReservationDeleteView.as_view(), name='all_res_del'),
    path('delres/<int:pk>', views.ReservationDeleteView.as_view(), name='del_res'),
    path('edit_reservation/<int:pk>', views.ReservationCreateView.as_view(), name='edit_res'),




]
