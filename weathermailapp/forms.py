from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()

class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'location')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')