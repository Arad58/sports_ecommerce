import pytest
from services import AuthService
from models import User

@pytest.fixture
def user():
    return UserProfile.objects.create_user(username='arad11', email='arad11@example.com', password='Arad2006!')

@pytest.fixture
def auth_service():
    return AuthService()

def test_signup(auth_service, user):
    response = auth_service.signup('arad11', 'Arad2006!')
    assert response['message'] == 'User has been created!'
    created_user = UserProfile.objects.get(username='arad11')
    assert created_user.username == 'arad11'
    assert created_user.email == 'arad11@example.com'

def test_signup_user_exists(auth_service, user):
    response = auth_service.signup('arad11', 'Arad2006!')
    assert response['message'] == 'User already does exist.'
    with pytest.raises(Exception):
        auth_service.signup('arad11', 'Arad2006!')

def test_login_success(auth_service, user):
    response = auth_service.login('arad11', 'Arad2006!')
    assert response['message'] == 'Login successful!'
    logged_in_user = UserProfile.objects.get(username='arad11')
    assert logged_in_user is not None
    assert logged_in_user.username == 'arad11'

def test_login_invalid_credentials(auth_service, user):
    response = auth_service.login('arad11', 'wrongpassword')
    assert response['message'] == 'Invalid credentials'
    with pytest.raises(ValueError, match="Invalid credentials"):
        auth_service.login('arad11', 'wrongpassword')

def test_logout(auth_service, user):
    response = auth_service.logout(user.id)
    assert response['message'] == 'User has been logged out!'
    logged_out_user = UserProfile.objects.get(id=user.id)
    assert logged_out_user.is_authenticated is False