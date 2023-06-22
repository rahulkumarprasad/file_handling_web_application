from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserCreateFrm(forms.Form):
    '''User create form for storing user data to user moedl and it will be used for validating request data'''
    first_name = forms.CharField(label="First Name", max_length=100, 
                                    widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(label="Last Name", max_length=100, 
                                    widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(label="Email", max_length=100, 
                                    widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="User-Name", max_length=100, 
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),max_length=20)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),max_length=20)

    def clean_password(self):
        # condition for password validation
        pasd = self.cleaned_data["password"]
        if len(pasd) < 8:
            raise ValidationError("Password should be at least 8 char long")
        return pasd

    def clean_username(self):
        # condition for username validation
        usname = self.cleaned_data["username"]
        if len(usname) < 6:
            raise ValidationError("User name should be at least 6 char long")
        return usname
        
    def clean_confirm_password(self):
        # condition for confirm_password validation
        pasd = self.cleaned_data["password"]
        cnf_pasd = self.cleaned_data["confirm_password"]
        
        if pasd != cnf_pasd:
            raise ValidationError("Password does not match!")
        return cnf_pasd

    def save(self):
        # creating user data and setting its password into user model
        new_user  =  User(username = self.cleaned_data["username"], 
        first_name=self.cleaned_data["first_name"], last_name = self.cleaned_data["last_name"],
        email = self.cleaned_data["email"])
        new_user.set_password(self.cleaned_data["password"])
        new_user.save()
        return new_user