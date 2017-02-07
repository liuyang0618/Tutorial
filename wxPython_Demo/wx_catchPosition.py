#encoding:utf-8
__author__ = 'Administrator'

"""
需求：
捕获窗体坐标
    创建一个窗体，该窗体中有一个文本框，当鼠标在窗体中移动时，文本框显示当前鼠标的位置
"""

import wx

#创建框架类
class myFrame(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title=u'第一个窗体',pos =(100, 200),  size=(300,300))
        #创建一个面板
        panel = wx.Panel(self)
        #将鼠标移动的事件绑定到自定义的OnMove方法
        panel.Bind(wx.EVT_MOTION, self.onMove)
        #显示一个静态文本框
        wx.StaticText(parent=panel, label="Pos:", pos=(10,20))
        #创建一个文本框输入框
        self.posCtrl = wx.TextCtrl(parent=panel, pos=(40,20))

    def onMove(self, event):
        #获取事件的位置
        pos = event.GetPosition()
        #给文本输入框添加内容
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

if __name__ == "__main__":
    #定义应用程序类的一个对象
    app = wx.App()
    #创建框架对象
    frame = myFrame(None)
    #框架显示
    frame.Show(True)
    #创建事物循环
    app.MainLoop()

