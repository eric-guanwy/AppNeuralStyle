# -*- coding: utf-8 -*-
# filename: media.py
from basic import Basic
import urllib2
import json
import poster.encode
from poster.streaminghttp import register_openers

class Media(object):
    def __init__(self):
        register_openers()
    def upload(self, accessToken, filePath, mediaType):
        try:
            openFile = open(filePath, "rb")
        except:
            print "openfile failed!"
        param = {'media': openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        print "upload postUrl: ",postUrl
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        #print "urlResp.read: ", urlResp.read()
        #rspdata = urlResp.read()
        jsonDict = json.loads(urlResp.read())
        #print "rspdata: ",type(rspdata),rspdata
        print "jsonDict: ",jsonDict
        return jsonDict['media_id']

        #print "media_id:",rspdata["media_id"]

    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        print "postUrl:",postUrl
        urlResp = urllib2.urlopen(postUrl)
        print "urlResp:",urlResp

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()
            mediaFile = file("media/test_media_%s.jpg"%mediaId, "wb")
            mediaFile.write(buffer)
            print "get successful"
"""
if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = "/home/ubuntu/webpy/media/BSNAP300.jpg"   #请安实际填写
    mediaType = "image"
    myMedia.upload(accessToken, filePath, mediaType)

    mediaId = "g86ztIwIhYzncf3HhmU8yJ_b7ps9ydJc3q3KbhNbIlGseh4hPLV7fLE4KuJOnNlS"
    myMedia.get(accessToken, mediaId)
"""