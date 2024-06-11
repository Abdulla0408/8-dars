from django import forms
from .models import User, Student


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))

    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password', 'user_role')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password


class Profile_Edit_Form(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Address"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "Image"}))
    email = forms.EmailField(widget=forms.EmailInput({"class": "form-control", "placeholder": "Email"}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'address', 'image', 'email')


class StudentEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput({"class": "form-control"}))

    class Meta:
        model = Student
        fields = ('date_of_birth', 'team')


class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Old password"}))
    new_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "New password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm password"}))

    def clean_confirm_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_password = self.cleaned_data['confirm_password']

        if new_password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return confirm_password
