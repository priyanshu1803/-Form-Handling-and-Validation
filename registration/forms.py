from django import forms

from django.core import validators
#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    Address = forms.CharField(required = False, )
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput,validators = [validators.MinLengthValidator(6)])
    re_password = forms.CharField(widget = forms.PasswordInput, required = False)
   
   
#Validation 

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

   