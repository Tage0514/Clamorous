from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.wechat.models import BindWechat
from apps.base_info.models import BaseInformation
import hashlib
import time
from apps.wechat.receive import parse_xml
from apps.wechat import receive, reply
from django.db.models import Q


@csrf_exempt
def weixin_main(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'wtage'

        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print('[token, timestamp, nonce]', hashlist)
        hashstr = ''.join([s for s in hashlist]).encode(
            'utf-8')  #这里必须增加encode('utf-8'),否则会报错
        print('hashstr befor sha1', hashstr)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print('hashstr sha1', hashstr)
        if hashstr == signature:
            return HttpResponse(echostr)  #必须返回echostr
        else:
            return HttpResponse('error')  #可根据实际需要返回
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)


def autoreply(request):
    try:
        webData = str(request.body, encoding='utf-8')
        print("Handle Post webdata is ", webData)
        recMsg = parse_xml(webData)
        if isinstance(recMsg, receive.Msg):
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.MsgType == 'text':
                if recMsg.Content == '绑定':
                    content = '请输入绑定+学号，例如：绑定+2019000111'
                elif recMsg.Content[0:3] == '绑定+':

                    temp = recMsg.Content[3:]
                    data = BaseInformation.objects.filter(stu_id=temp).values()
                    # print(data)
                    if data is not None:
                        bdata = BindWechat.objects.filter(
                            Q(stu_id=temp) | Q(stu_openid=toUser)).values()
                        # print(bdata)
                        if bdata.exists():
                            content = "当前微信号或学号已被绑定，请联系管理员！"
                        else:
                            print(data[0]['stu_id'])
                            binddata = BindWechat()
                            binddata.stu_id = data[0]['stu_id']
                            binddata.stu_name = data[0]['stu_name']
                            binddata.stu_class = data[0]['stu_class']
                            binddata.stu_openid = toUser
                            binddata.save()
                            content = "绑定成功!"
                    else:
                        content = "学号不存在！请重新输入"
                else:
                    # print(recMsg.Content)
                    content = recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            if recMsg.MsgType == 'image':
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
        if isinstance(recMsg, receive.EventMsg):
            if recMsg.Event == 'CLICK':
                if recMsg.Eventkey == 'mpGuide':
                    content = u"编写中，尚未完成".encode('utf-8')
                    replyMsg = TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
        print("这里是1")
        return Msg().send()
    except (Exception) as Argment:
        return Argment
