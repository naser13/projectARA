from django.contrib import admin
from head_master.models import HeadMaster
from school.models import School


class SchoolInline(admin.StackedInline):
    model = School
    max_num = 1


class HeadAdmin(admin.ModelAdmin):
    fieldsets = [
        ('اطلاعات شخصی', {'fields': ['first_name', 'last_name', 'national_ID', 'father_name']}),
        ('مدرسه', {'fields': ['school']})
    ]
admin.site.register(HeadMaster, HeadAdmin)