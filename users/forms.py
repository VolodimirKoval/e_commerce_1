from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введіть ваше ім`я',
    #         }
    #     )
    # )
    #
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введіть ваше прізвище',
    #         }
    #     )
    # )
    #
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введіть ваше ім`я користувача',
    #         }
    #     )
    # )
    #
    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введіть ваш email *your_email@example.com*',
    #         }
    #     )
    # )
    #
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введіть пароль',
    #         }
    #     )
    # )
    #
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Підтвердіть пароль',
    #         }
    #     )
    # )
    #


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
        )
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    