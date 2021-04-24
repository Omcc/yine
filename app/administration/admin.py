from django.contrib import admin
from administration.models import Address
from administration.forms import AddressAdminForm
from administration.models import School,ClassRoom,Lecture,LectureSchedule

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
admin.site.register(Address)
admin.site.register(School)
admin.site.register(ClassRoom)
admin.site.register(Lecture)
admin.site.register(LectureSchedule)