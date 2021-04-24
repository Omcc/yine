from django.db import models

from django.utils.translation import ugettext as _
from django.contrib.auth.models import User as Auth_User

from smart_selects.db_fields import (
    ChainedForeignKey,
    ChainedManyToManyField,
    GroupedForeignKey,
)
#abstract models#

class AuthUser(models.Model):
    auth_user = models.ForeignKey(Auth_User, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class PersonalInformations(models.Model):
    GENDER_IN_PERSONALINFO_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
        ('U', _('Unknown'))
    ]
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    telephone = models.CharField(max_length=20,null=False,blank=False)
    gender = models.CharField(choices=GENDER_IN_PERSONALINFO_CHOICES,max_length=2)
    class Meta:
        abstract = True

#Sub Models#

class Country(models.Model):
    binary_code = models.CharField(max_length=2,null=False)
    triple_code = models.CharField(max_length=3,null=False)
    country_name = models.CharField(max_length=100,null=False)
    phone_code = models.CharField(max_length=6,null=False)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100,null=False)
    plate_no = models.CharField(max_length=2,null=False)
    phone_code = models.CharField(max_length=7, null=False)

    def __str__(self):
        return self.city_name

class County(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    county_name = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.county_name
class District(models.Model):
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100,null=False)
    zip_code = models.CharField(max_length=20,null=False)
class Address(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    city = ChainedForeignKey(
        "City",
        chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
    )
    county =ChainedForeignKey(
        "County",
        chained_field="city",
        chained_model_field="city",
        show_all=False,
        auto_choose=True,
    )
    district = models.CharField(max_length=100,null=False)
    full_address = models.CharField(max_length=100,null=False)
    postal_code = models.IntegerField(max_length=10,null=False)

    def __str__(self):
        return "{} {} {}".format(self.city,self.county,self.full_address)




###########


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50,unique=True)
    telephone = models.CharField(max_length=50,unique=True)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name


class Manager(AuthUser,PersonalInformations):
    school = models.ManyToManyField(School)
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)


class Teacher(AuthUser,PersonalInformations):
    school = models.ManyToManyField(School)
    title = models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return "{} {} {}".format(self.title,self.first_name,self.last_name)

class Lecture(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    grade = models.IntegerField()
    branch = models.CharField(max_length=2)
    lecture = models.ManyToManyField(Lecture,through='LectureSchedule')

    def __str__(self):
        return "{} {}/{}".format(self.school,self.grade,self.branch)

class LectureSchedule(models.Model):
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    start=models.DateTimeField(null=True)
    end=models.DateTimeField(null=True)

    def __str__(self):
        return "{} {}".format(self.classroom,self.lecture)

class Student(AuthUser,PersonalInformations):
    student_id = models.CharField(max_length=20, null=False)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return "{} {} ".format(self.first_name,self.last_name)

class Parent(AuthUser,PersonalInformations):
    students = models.ManyToManyField(Student)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)








