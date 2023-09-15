 # first import forms
from django import forms

# now import UserCreationForm for create the user and Customize, its default django form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User

#for profile
from .models.profile import Profile

# for dash_
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Choose a Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput({'class': 'form-control'}))
    class Meta(UserCreationForm):
        model = User # User.objects.all(), it will use djnago model
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name':'Fisrt Name', 'last_name': 'Last name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   }

# here no role of model becausue its made by api so we import only AuthenticationForm and UsernameField
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete':'current-password', 'class':'form-control'}))

class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#for updating user profile, but before import Profile
class UserUpdate(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
# Now import both form in views.py