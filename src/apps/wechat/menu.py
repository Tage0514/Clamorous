# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
from basic import Basic


class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
             {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "培养信息",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "研究生培养",
                        "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=1&sn=1e89c8f21a03235171ec6d162d250c54"
                    },
                    {
                        "type": "view",
                        "name": "德育培养",
                        "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=2&sn=f053d1dde0e5985f87274a40931dc8ff"
                    },
                    {
                        "type": "view",
                        "name": "党建信息",
                        "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=3&sn=39b761461d0245c7bf87fb2d44d25846"
                    },
		    {
			"type":"view",
			"name":"毕业就业",
			"url":"https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=4&sn=02f2b4aa5bab342e02b6c54a95636918"	
		    }
                ]
            },
	    {
		"name": "我", 
           	"sub_button": 
		[
                    {
                        "type": "view", 
                        "name": "已参加活动", 
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxd336a1cb1065e187&redirect_uri=http://wtage.cn/activity/pai&response_type=code&scope=snsapi_base&state=STATE"
                    }, 
                    {
                        "type": "view", 
                        "name": "帮助", 
                        "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=1&sn=1e89c8f21a03235171ec6d162d250c54" 
                    }, 
                    {
                        "type": "view", 
                        "name": "我的培养计划", 
                        "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=1&sn=1e89c8f21a03235171ec6d162d250c54"
                    },
		    {
			"type": "view",
			"name": "我的成果",
			"url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=1&sn=1e89c8f21a03235171ec6d162d250c54"
		    }
                ]
	    }
	]
    }
    """
    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
