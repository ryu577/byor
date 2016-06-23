from __future__ import unicode_literals
from django import forms
from .models import Profile, Reviewer
from cuser.models import CUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CUser
        fields = ['first_name', 'last_name', 'email', 'password']
    repeat_password = forms.CharField(max_length=128)

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['repeat_password']:
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

    photo = forms.ImageField(required=False)


class ReviewerForm(forms.ModelForm):
    class Meta:
        model = Reviewer
        fields = ['position', 'current_job', 'previous_job', 'total_years', 'bs_subject', 'bs_university', 'ms_subject',
                  'ms_university', 'phd_subject', 'phd_university', 'linkedin', 'summary']