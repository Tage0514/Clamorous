from django.contrib import admin
from apps.get_activity_info.models import SignUpInfo, ParticipationRecord
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.


class SignUpInfoAdmin(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                    'stu_status', 'act_score', 'act_time')

    search_fields = ('stu_name', 'act_name', 'stu_id')
    list_filter = ["act_name"]
    date_hierarchy = 'act_time'


class ParticipationRecordAdmin(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                    'stu_status', 'act_score', 'act_time')
    list_editable = ["act_score"]
    search_fields = ('stu_name', 'act_name', 'stu_id')
    list_filter = ["act_name"]
    date_hierarchy = 'act_time'


admin.site.register(SignUpInfo, SignUpInfoAdmin)

admin.site.register(ParticipationRecord, ParticipationRecordAdmin)

admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理'
admin.site.index_title = '后台站点管理'
