from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password, get_hasher
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import UserForm, ProfileForm
from .models import Profile
from cuser.models import CUser


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = ProfileForm(request.POST, request.FILES, prefix='profile')
        if uf.is_valid() * upf.is_valid():
            user = CUser(
                first_name=uf.cleaned_data['first_name'],
                last_name=uf.cleaned_data['last_name'],
                email=uf.cleaned_data['email'],
                password=make_password(uf.cleaned_data['password']),
                is_active=1
            )
            user.save()
            profile = Profile(
                photo=request.FILES['profile-photo'],
                phone_number=upf.cleaned_data['phone_number'],
                date_of_birth=upf.cleaned_data['date_of_birth'],
                is_male=upf.cleaned_data['is_male'],
                street=upf.cleaned_data['street'],
                unit=upf.cleaned_data['unit'],
                city=upf.cleaned_data['city'],
                state=upf.cleaned_data['state'],
                zipcode=upf.cleaned_data['zipcode'],
                type=2,
            )
            # profile = upf.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect('/')
    else:
        uf = UserForm(prefix='user')
        upf = ProfileForm(prefix='profile')
    return render_to_response('accounts/register.html',
                              dict(userform=uf,
                              profileform=upf),
                              context_instance=RequestContext(request))