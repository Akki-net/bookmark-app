from django import forms
from django.contrib.auth.models import User
from .models import Profile
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class UserRegistration(forms.ModelForm):
    password = forms.CharField(label="Password", 
                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", 
                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']
    def clean_email(self):
        data = self.cleaned_data['email']
        if data != "" and User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.filter(email=data)\
                .exclude(id=self.instance.id)
        if data != "" and qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']