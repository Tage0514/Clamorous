from django.http import HttpResponse
from django.shortcuts import render
from apps.get_activity_info.models import SignUpInfo, ParticipationRecord
from apps.base_info.models import BaseInformation, BindWechat
import hashlib
import time
from apps.wechat.receive import parse_xml
from apps.wechat import receive, reply
from apps.get_activity_info.getopenid import get_session_key, get_code


def pose_activity_info(request):
    av_catalog = {
        'list1': [{
            'act_name': '新生教育',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2018-09'
        }, {
            'act_name': '校庆活动',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-01'
        }, {
            'act_name': '雄安新区汇报',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-03'
        }],
        'list2': [{
            'act_name': '新生教育',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2018-09'
        }, {
            'act_name': '校庆活动',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-01'
        }, {
            'act_name': '雄安新区汇报',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-03'
        }]
    }
    if request.method == 'GET':
        # print(1)
        code = request.GET.get('code')
        # print(code)
        # if code is None:
        #     print(2)
        #     code = get_code()
        #     print(code)
        flag, openid = get_session_key(code)
        # print(openid)
        if flag:
            bindwechardata = BindWechat.objects.filter(
                stu_openid=openid).values()
            stuid = bindwechardata[0]['stu_id']
            list1 = ParticipationRecord.objects.filter(stu_id=stuid).values()
            list2 = MoralActivity.objects.filter(stu_id=stuid).values()
            context = {"list1": list1, "list2": list2}
            # return HttpResponse(list1)
            # return HttpResponse(webData)
            return render(request, 'get_activity_info/showinfo.html', context)
            # return render(request, 'get_activity_info/warm_showinfo.html')
            # print(stuid)
        else:
            return render(request, 'get_activity_info/warm_showinfo.html')

    return render(request, 'get_activity_info/showinfo.html')


def get_activity_info(request, name, time):
    act_name = name
    act_time = time
    context = {"act_name": act_name, "act_time": act_time}
    return render(request, 'get_activity_info/getinfo.html', context)


def get_activity_info_base(request):
    return render(request, 'get_activity_info/getinfo.html')


def activity(request):
    return render(request, 'get_activity_info/activity.html')


def data_post(request):
    if request.method == "POST":
        stu_name = request.POST.get('stu_name')
        stu_id = request.POST.get('stu_id')
        stu_class = request.POST.get('stu_class')
        act_name = request.POST.get('act_name')
        act_time = request.POST.get('act_time')
        stu_status = request.POST.get('stu_status')

        base_info_stu_id = BaseInformation.objects.values_list(
            'stu_id', flat=True)
        base_info_stu_name = BaseInformation.objects.values_list(
            'stu_name', flat=True)
        base_info_stu_class = BaseInformation.objects.values_list(
            'stu_class', flat=True)
        # for baseinfoid in base_info_stu_id:

        if stu_id in base_info_stu_id and stu_name in base_info_stu_name and stu_class in base_info_stu_class:
            signup = SignUpInfo()
            signup.stu_name = stu_name
            signup.stu_id = stu_id
            signup.stu_class = stu_class
            signup.act_name = act_name
            signup.act_time = act_time
            signup.stu_status = stu_status
            signup.save()
            return render(request, 'get_activity_info/success.html')

        else:
            return render(request, 'get_activity_info/warn.html')

        # print(type(base_info_stu_id))
        # print(base_info_stu_id)
        # return render(request, 'get_activity_info/success.html')
        # return render(request, 'get_activity_info/warn.html')
