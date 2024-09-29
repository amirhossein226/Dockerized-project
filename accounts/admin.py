from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile
# Register your models here.

UserModel = get_user_model()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',
                    'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    ordering = ['-date_joined']
    search_fields = ['username', 'email', 'first_name']


admin.site.register(UserModel, UserAdmin)
