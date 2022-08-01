from django import forms
from django.contrib.auth.models import User



#from django.core.exceptions import ValidationError



class UserCreateForm(forms.ModelForm):
    password = forms.CharField(required=True, max_length=128, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(required=True, max_length=128, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))
    first_name = forms.CharField(min_length=3, required=True, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(min_length=3, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    username = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'e-mail'}))
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'password2',
        )




class LoginForm(forms.Form):
    username = forms.EmailField(max_length=256, widget=forms.EmailInput(attrs={'placeholder': 'e-mail'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'hasło'}))





class UserEditForm(forms.ModelForm):
    old_password =forms.CharField(required=True, max_length=128, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Stare hasło'}))
    password = forms.CharField(required=True, max_length=128, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(required=True, max_length=128, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))
    first_name = forms.CharField(min_length=3, required=True, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(min_length=3, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'old_password',
            'password',
            'password2',
        )

    def clean(self):
        super().clean()
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Hasła różnią się ')




# class DonationForm(forms.Form):
#     class Meta:
#         model = Donation
#         fields = (
#            'categories',
#            'quantity',
#            'institution',
#            'address',
#            'city',
#            'zip_code',
#            'phone_number',
#            'pick_up_date',
#            'pick_up_time',
#            'pick_up_comment',
#             )