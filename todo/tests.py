import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import ToDo
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your tests here.

client = APIClient()

@pytest.mark.django_db
class TestToDoAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Assuming you have a user setup for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        client.force_authenticate(user=self.user)

    def test_create_todo(self):
        data = {
            'title': 'Test ToDo',
            'description': 'This is a test description',
            'is_completed': False
        }

        response = client.post(reverse('todo-list-create'), data, format='json')
        assert response.status_code == 201
        assert ToDo.objects.count() == 1
        assert ToDo.objects.get().title == 'Test ToDo'
        assert ToDo.objects.get().user == self.user

    def test_get_todos(self):
        ToDo.objects.create(user=self.user, title='My ToDo', description='Test', is_completed=False)
        response = client.get(reverse('todo-list-create'))
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert len(response.data) == ToDo.objects.count()  


    def test_update_todo(self):
        todo = ToDo.objects.create(user=self.user, title='Old Title', description='Old Description', is_completed=False)
        data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'is_completed': True
        }

        response = client.put(reverse('todo-detail', kwargs={'pk': todo.id}), data, format='json')
        assert response.status_code == 200
        todo.refresh_from_db()
        assert todo.title == 'Updated Title'
        assert todo.description == 'Updated Description'
        assert todo.is_completed is True

    def test_delete_todo(self):
        todo = ToDo.objects.create(user=self.user, title='To Delete', description='Delete this', is_completed=False)
        response = client.delete(reverse('todo-detail', kwargs={'pk': todo.id}))
        assert response.status_code == 204
        assert ToDo.objects.count() == 0  

    def test_user_cannot_access_others_todos(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        ToDo.objects.create(user=other_user, title='Other User ToDo', description='Should not be accessible', is_completed=False)

        response = client.get(reverse('todo-list-create'))

        assert response.status_code == 200
        assert len(response.data) == 0 


@pytest.mark.django_db
class TestTokenAuth:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.auth_client = APIClient()
        self.auth_client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.unauth_client = APIClient()

    def test_token_login(self):
        client = APIClient()
        response = client.post(reverse('api_token_auth'), {'username': 'testuser', 'password': 'testpassword'}, format='json')
        assert response.status_code == 200
        assert 'token' in response.data

    def test_access_with_token(self):
        response = self.auth_client.get(reverse('todo-list-create'))
        assert response.status_code == 200

    def test_access_without_token(self):
        response = self.unauth_client.get(reverse('todo-list-create'))
        assert response.status_code == 401