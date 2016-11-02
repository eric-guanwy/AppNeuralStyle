# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import reply
import receive
import web
from basic import Basic
import media

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "neuralstyle"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                #print "return:%s"%echostr
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()            
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)

            if isinstance(recMsg, receive.Msg):
                if recMsg.MsgType == 'text':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    myMedia = media.Media()
                    accessToken = Basic().get_access_token()
                    piclist=["15","21","25","47","57","77"]
                    if recMsg.Content in piclist:
                        print "recMsg.Content: ",recMsg.Content
                        filePath = recMsg.Content+".jpg"
                        print "filePath: ",filePath
                        mediaType = "image"
                        try:
                            MediaId=myMedia.upload(accessToken, filePath, mediaType)
                        except:
                            print "myMedia.upload exception!"
                        replyMsg = reply.ImageMsg(toUser, fromUser, MediaId)
                        print "replyMsg: ",replyMsg
                        return replyMsg.send()
                    elif recMsg.Content == "all pic":
                        content = piclist
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    else:
                        content = "hello..."
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()

                if recMsg.MsgType == 'image':
                    myMedia = media.Media()
                    accessToken = Basic().get_access_token()
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    MediaId = recMsg.MediaId
                    myMedia.get(accessToken, MediaId)
                    filePath = "19a21.jpg"
                    print filePath
                    mediaType = "image"
                    try:
                        MediaId=myMedia.upload(accessToken, filePath, mediaType)
                    except:
                        print "myMedia.upload exception!"                    
                    replyMsg = reply.ImageMsg(toUser, fromUser, MediaId)
                    print "replyMsg: ",replyMsg
                    return replyMsg.send()
                else:
                    print "else reply.Msg : ",reply.Msg
                    return reply.Msg.send()
            else:
                print "Holdon..."
                return "success"
        except Exception, Argment:
            print "Exception..."
            return Argment