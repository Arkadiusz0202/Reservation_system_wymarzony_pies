import pytest
from django.contrib.auth.models import User
from django.urls import reverse



def test_client(client):
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.django_db
def test_customer_create_view(client, user):
    client.post(reverse('registration'), {'username': 'arek', 'password1': 'testowe', 'password2': 'testowe'})
    user = User.objects.get(username='arek')
    assert user.is_authenticated


@pytest.mark.django_db
def test_add_location_view(client, user):
    client.login(username='arek', password='testowe')
    response = client.get(reverse('Location'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_location_view(client, location):
    client.login(username='arek', password='testowe')
    response = client.post(reverse('del_loc', args=[location.id]), data={'delete': 'TAK'})
    assert response['location'] == reverse('Location')


@pytest.mark.django_db
def test_create_trainer_view(client, user, trainers):
    client.login(username='arek', password='testowe')
    response = client.get(reverse('add_trainer'))
    assert response.status_code == 200
    assert list(response.context['objects']) == trainers


@pytest.mark.django_db
def test_delete_trainer_view(client, trainer):
    client.login(username='arek', password='testowe')
    response = client.post(reverse('del_trainer', args=[trainer.id]), data={'delete': 'TAK'})
    assert response.url == reverse('add_trainer')


@pytest.mark.django_db
def test_create_training_view(client, user, training):
    client.login(username='arek', password='testowe')
    response = client.get(reverse('add_training'))
    assert response.status_code == 200
    assert response.context['objects'][0] == training


@pytest.mark.django_db
def test_training_view(client):
    client.login(username='arek', password='testowe')
    assert client.get(reverse('all_trainings')).status_code == 200


@pytest.mark.django_db
def test_training_delete_view(client, training):
    client.login(username='arek', password='testowe')
    response = client.post(reverse('del_training', args=[training.id]), data={'delete': 'TAK'})
    assert response.url == reverse('add_training')


@pytest.mark.django_db
def test_reservation_create_view(client, user, reservation):
    client.login(username='arek', password='testowe')
    response = client.post(reverse('add_reservation'), data=reservation.__dict__)
    assert response.status_code == 200





@pytest.mark.django_db
def test_reservation_view(client, user):
    client.login(username='arek', password='testowe')
    assert client.get(reverse('reservations')).status_code == 200