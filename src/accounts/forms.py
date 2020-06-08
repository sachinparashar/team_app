from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

User = get_user_model()

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        qs = User.objects.filter(username=username)
        if qs.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name.isalnum() == False:
            raise ValidationError("Enter valid First Name")
        return first_name
            

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name.isalnum() == False:
            raise ValidationError("Enter valid Last Name")
        return last_name

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        qs = User.objects.filter(email=email)
        if qs.count():
            raise  ValidationError("Email already exists")
        
        try:
            valid_email = validate_email(email)
            return email
        except:
            raise ValidationError("Email is not valid")
    