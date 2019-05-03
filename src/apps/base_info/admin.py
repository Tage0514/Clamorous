from django.contrib import admin
from apps.base_info.models import BaseInformation


class BaseInforAdmin(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_gender', 'stu_class',
                    'stu_college', 'stu_graduation')


admin.site.register(BaseInformation,BaseInforAdmin)