# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json

class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0
    def __real_get_access_token(self):
        #appId = "wxb8ec3ac0f775f8e6"
        #appSecret = "4727969c9f1b21f138433edcff25bf5e"
        appId = "wx1aeaeddc623ee631"
        appSecret = "4f838dcd039b124c762f2b03358f6181"

        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
               "client_credential&appid=%s&secret=%s" % (appId, appSecret))
        print "basic postUrl: ",postUrl
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        
        self.__accessToken = urlResp['access_token']
        #print "accessToken: ", self.__accessToken
        self.__leftTime = urlResp['expires_in']

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken

    def run(self):
        while(True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()