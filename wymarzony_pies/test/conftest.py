import pytest
from django.contrib.auth.models import User
from django.test import Client
from wymarzony_pies.models import Trainer, Location, Training, Reservation


@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user():
    user = User.objects.create(username='arek', is_superuser=True)
    user.set_password('testowe')
    user.save()
    return user

@pytest.fixture
def trainers():
    items = []
    for name, description in [('test1', 'opis1'), ('test2', 'opis2'), ('test3', 'opis3')]:
        data = Trainer.objects.create(name=name, description=description)
        items.append(data)
    return items

@pytest.fixture
def trainer():
    return Trainer.objects.create(name='testowy', description='description')

@pytest.fixture
def location():
    return Location.objects.create(name='test', address='test2', open_form=1, open_to=2)

@pytest.fixture
def training():
    return Training.objects.create(name='test', description='test1')


@pytest.fixture
def reservation():
    fake_user = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
    fake_trainer = Trainer.objects.create(name='test', description='test')
    fake_training = Training.objects.create(name='test1', description='test1')
    fake_location = Location.objects.create(name='test2', address='test2', open_form=1, open_to=2)
    return Reservation.objects.create(user=fake_user, trainer=fake_trainer, training=fake_training, location=fake_location,
                                      date_of_reservation='2000-01-10', res_from=1, res_to=2)

