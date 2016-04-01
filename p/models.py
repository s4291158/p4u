from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

ROLE_CHOICES = [
    ('user', 'user'),
    ('parkee', 'parkee'),
    ('parker', 'parker'),
    ('both', 'both'),
]


class Landed(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    suburb = models.CharField(max_length=40)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    price = models.FloatField()
    when = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class BaseUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=20, null=True, blank=True)


class Address(models.Model):
    street_address = models.CharField(max_length=200, null=True, blank=True)
    suburb = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)

    formatted = models.CharField(max_length=200)
    position = GeopositionField()

    def __str__(self):
        return self.formatted


class Parker(models.Model):
    baseUser = models.OneToOneField(BaseUser)

    def __str__(self):
        return self.baseUser.username


class Parkee(models.Model):
    baseUser = models.OneToOneField(BaseUser)
    abn = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.baseUser.username


class Carpark(models.Model):
    parkee = models.ForeignKey(Parkee, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    price = models.FloatField(default=0)
    verified = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.address.formatted


class Area(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
