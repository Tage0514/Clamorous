from django.http import HttpResponse
from django.shortcuts import render


def pose_activity_info(request):

    context = {"a": "nn", "b": "2", "c": "3"}
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

    return render(request, 'get_activity_info/showinfo.html', av_catalog)


def get_activity_info(request, name, time):
    act_name = name
    act_time = time
    context = {"act_name": act_name, "act_time": act_time}
    return render(request, 'get_activity_info/getinfo.html', context)


def get_activity_info_base(request):
     return render(request, 'get_activity_info/getinfo.html')


def activity(request):
    return render(request, 'get_activity_info/activity.html')
