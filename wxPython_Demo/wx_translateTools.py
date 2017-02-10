# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan  9 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
#import urllib.request
#import urllib.parse

import urllib
import urllib2
import json

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"翻译软件", pos = wx.DefaultPosition, size = wx.Size( 500,459 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"C:\\Users\\Administrator\\Desktop\\ly.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        bSizer1.Add( self.m_bpButton1, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"原文：", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer1.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"翻译", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"译文：", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer1.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_button1OnButtonClick( self, event ):
        #显示处理中
        self.m_textCtrl2.SetValue(u"处理中...")
        content = self.m_textCtrl1.GetValue()
        print(content)
        #有道翻译请求的url
        url= "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index"

        #发送请求
        data = {}
        data['type']='AUTO'
        data['i']=content
        data['doctype']='json'
        data['xmlVersion']='1.8'
        data['keyfrom']='fanyi.web'
        data['ue']='UTF-8'
        data['action']='FY_BY_CLICKBUTTON'
        data['typoResult']='true'

        #对请求的post参数进行格式转化为application/x-www-form-urlencoded
        #data =  urllib.parse.urlencode(data).encode('utf-8')
        data =  urllib.urlencode(data).encode('utf-8')  #转换为python2的代码

        #打开网页获得httpresponse对象
        #response = urllib.request.urlopen(url,data)
        response = urllib2.urlopen(url,data)  #转换为python2的代码

        #将utf-8 解码unicode
        html = response.read().decode('utf-8')
        #通过json将字节流数据转换为字典
        target = json.loads(html)

        print(u"翻译的结果为：%s" % (target['translateResult'][0][0]['tgt']))
        self.m_textCtrl2.SetValue(target['translateResult'][0][0]['tgt'])


if __name__ == "__main__":
    #定义应用程序类的一个对象
    app = wx.App()
    #创建框架对象
    frame = MyFrame1(None)
    #框架显示
    frame.Show(True)
    #创建事物循环
    app.MainLoop()