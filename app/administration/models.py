from django.db import models

from django.utils.translation import ugettext as _
from django.contrib.auth.models import User as Auth_User


#abstract models#

class AuthUser(models.Model):
    auth_user = models.ForeignKey(Auth_User, on_delete=models.CASCADE)
    class Meta:
        abstract = True

#Sub Models#

class Country(models.Model):
    binary_code = models.CharField(max_length=2,null=False)
    triple_code = models.CharField(max_length=3,null=False)
    country_name = models.CharField(max_length=100,null=False)
    phone_code = models.CharField(max_length=6,null=False)


class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100,null=False)
    plate_no = models.CharField(max_length=2,null=False)
    phone_code = models.CharField(max_length=7, null=False)

class County(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    county_name = models.CharField(max_length=50,null=False)








###########


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50,unique=True)
    telephone = models.CharField(max_length=50,unique=True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name


class Manager(AuthUser):
    first_name = models.CharField(max_length=30,null=False,blank=False)
    last_name = models.CharField(max_length=30,null=False,blank=False)





