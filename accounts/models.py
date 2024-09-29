from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class CusUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField("تاریخ تولد", blank=True, null=True)
    photo = models.ImageField(
        "عکس پروفایل",
        upload_to='user/%Y/%m/%d/',
        blank=True
    )
