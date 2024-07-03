from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password  = forms.CharField(label='Пароль', widget=forms.PasswordInput)