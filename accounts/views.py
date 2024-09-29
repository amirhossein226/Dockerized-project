from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserEditForm, ProfileEditForm
# Create your views here.
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib import messages
from django.urls import reverse


UserModel = get_user_model()


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'تغییرات شما با موفقیت اعمال شد.')
            return redirect(reverse("dashboard"))
        pass
    else:
        user_form = UserEditForm(
            instance=request.user
        )
        profile_form = ProfileEditForm(
            instance=request.user.profile
        )

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(
        request,
        'account/dashboard/edit.html',
        context
    )


@login_required
def dashboard(request):

    return render(
        request,
        'account/dashboard/dashboard_info.html',
        {'selected': 'dashboard'}
    )


def register_user(request):
    saved = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            Profile.objects.create(user=user)
            saved = True
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'registered': saved
    }

    return render(
        request,
        'account/registration.html',
        context,

    )
