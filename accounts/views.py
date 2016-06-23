from django.contrib.auth.hashers import make_password
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from .forms import UserForm, ProfileForm, ReviewerForm
from .models import Profile
from cuser.models import CUser


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        pf = ProfileForm(request.POST, request.FILES, prefix='profile')
        if uf.is_valid() * pf.is_valid():
            user = CUser(
                first_name=uf.cleaned_data['first_name'],
                last_name=uf.cleaned_data['last_name'],
                email=uf.cleaned_data['email'],
                password=make_password(uf.cleaned_data['password']),
                is_active=1
            )
            user.save()
            profile = Profile(
                phone_number=pf.cleaned_data['phone_number'],
                date_of_birth=pf.cleaned_data['date_of_birth'],
                is_male=pf.cleaned_data['is_male'],
                street=pf.cleaned_data['street'],
                unit=pf.cleaned_data['unit'],
                city=pf.cleaned_data['city'],
                state=pf.cleaned_data['state'],
                zipcode=pf.cleaned_data['zipcode'],
                type=3,  # User
            )
            try:
                photo = request.FILES['profile-photo']
            except MultiValueDictKeyError:
                pass
            profile.user = user
            profile.save()
            return HttpResponseRedirect('/')
    else:
        uf = UserForm(prefix='user')
        pf = ProfileForm(prefix='profile')
    return render_to_response('accounts/register.html',
                              dict(userform=uf,
                              profileform=pf),
                              context_instance=RequestContext(request))


def reviewer_register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        pf = ProfileForm(request.POST, request.FILES, prefix='profile')
        rf = ReviewerForm(request.POST, prefix='reviewer')
        if uf.is_valid() * pf.is_valid() * rf.is_valid():
            user = CUser(
                first_name=uf.cleaned_data['first_name'],
                last_name=uf.cleaned_data['last_name'],
                email=uf.cleaned_data['email'],
                password=make_password(uf.cleaned_data['password']),
                is_active=1
            )
            user.save()
            profile = Profile(
                phone_number=pf.cleaned_data['phone_number'],
                date_of_birth=pf.cleaned_data['date_of_birth'],
                is_male=pf.cleaned_data['is_male'],
                street=pf.cleaned_data['street'],
                unit=pf.cleaned_data['unit'],
                city=pf.cleaned_data['city'],
                state=pf.cleaned_data['state'],
                zipcode=pf.cleaned_data['zipcode'],
                type=2,  # Reviewer
            )
            try:
                photo = request.FILES['profile-photo']
            except MultiValueDictKeyError:
                pass
            profile.user = user
            profile.save()
            reviewer = rf.save(commit=False)
            reviewer.user = user
            reviewer.confirmed = 0;
            reviewer.save()
            return HttpResponseRedirect('/')
    else:
        uf = UserForm(prefix='user')
        pf = ProfileForm(prefix='profile')
        rf = ReviewerForm(prefix='reviewer')
    return render_to_response('accounts/reviewer-register.html',
                              dict(userform=uf,
                                   profileform=pf,
                                   reviewerform=rf),
                              context_instance=RequestContext(request))