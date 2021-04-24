from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from administration.models import Address
from administration.forms import AddressAdminForm
from administration.models import School,ClassRoom,Lecture,LectureSchedule,Teacher,Student,Parent

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm

class StudentAdmin(admin.ModelAdmin):
    list_display=['get_name','link_to_classroom','get_phone',]
    list_filter = ['classroom__school',]

    def link_to_classroom(self,obj):
        link = reverse("admin:administration_classroom_change",args=[obj.classroom.id])
        return format_html('<a href="{}">{}</a>', link, obj.classroom)

    link_to_classroom.admin_order_field = 'classroom'
    link_to_classroom.short_description = 'Classroom'

    def get_name(self,obj):
        return obj
    get_name.admin_order_field = 'name'
    get_name.admin_short_description= 'name'
    def get_phone(self,obj):
        return obj.telephone
    get_phone.admin_order_field = 'Telephone'
    get_phone.admin_short_description= 'Telephone'

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['get_name','student_number',]
    def student_number(self,obj):
        return obj.student_set.count()
    def get_name(self,obj):
        return obj

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'classroom_number','student_number',]

    def get_name(self, obj):
        return obj
    def classroom_number(self, obj):
        return obj.classroom_set.count()

    def student_number(self,obj):
        classrooms = obj.classroom_set.all()
        total = 0
        for classroom in classrooms:
            total += classroom.student_set.count()
        return total
class ParentAdmin(admin.ModelAdmin):
    list_display = ['get_name','get_phone',]
    def get_phone(self,obj):
        return obj.telephone
    def get_name(self,obj):
        return obj

admin.site.register(Address)
admin.site.register(School,SchoolAdmin)
admin.site.register(ClassRoom,ClassRoomAdmin)
admin.site.register(Lecture)
admin.site.register(LectureSchedule)
admin.site.register(Teacher)
admin.site.register(Student,StudentAdmin)
admin.site.register(Parent,ParentAdmin)
