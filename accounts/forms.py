from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

UserModel = get_user_model()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'email',
            'first_name',
            'last_name',
        ]

    def clean_email(self):
        data = self.cleaned_data['email']
        query = UserModel.objects.filter(
            email=data
        ).exclude(
            id=self.instance.id
        )

        if query.exists():
            raise forms.ValidationError("این ایمیل در حال حاضر موجود می باشد")

        return data


class ProfileEditForm(forms.ModelForm):
    date_of_birth = JalaliDateField(
        label="تاریخ تولد", widget=AdminJalaliDateWidget)

    class Meta:
        model = Profile
        fields = [
            'date_of_birth',
            'photo'
        ]


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="تکرار رمز عبور", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = [
            'email',
            'username',
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("رمز عبور ها یکسان نیستند!")
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if UserModel.objects.filter(email=data).exists():
            raise forms.ValidationError("کاربری با این ایمیل موجود می باشد.")
        return data
