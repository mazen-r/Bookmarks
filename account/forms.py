from django import forms




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # PasswordInput widget is used to make browser treats it as a password input
