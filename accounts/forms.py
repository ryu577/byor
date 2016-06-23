from __future__ import unicode_literals
from django import forms
from .models import Profile
from cuser.models import CUser
from datetimewidget.widgets import DateWidget


class UserForm(forms.ModelForm):
    class Meta:
        model = CUser
        fields = ['first_name', 'last_name', 'email', 'password']
    repeat_password = forms.CharField(max_length=128)

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['password_repeat']:
            self._errors['password'] = ['Password do not match']
            del form_data['password']
            del form_data['repeat_password']
        if CUser.objects.filter(email=form_data['email']).exists():
            self._errors['email'] = ['Email already exist']
        return form_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'is_male', 'date_of_birth', 'date_of_birth', 'street', 'unit', 'city', 'state', 'zipcode']
        widgets = {
            'date_of_birth': DateWidget(attrs={'id': "id-profile-date_of_birth"}, bootstrap_version=3)
        }
    photo = forms.ImageField(required=False)
