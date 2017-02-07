#encoding:utf-8

__author__ = 'Administrator'

"""
需求：
求和
详情说明：用文本框接收用户输入的变量n的值，计算1~n的累加结果，再将结果显示到另一个文本框中。
例如：计算1+2+......+n, 数据输入和输出都是用文本框
"""

#导入wx库
import wx

#定义一个框架类
class myFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=u'求n的累加',pos=(100,200),size=(400,600))  #style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX)
        #创建一个面板
        panel = wx.Panel(self)
        #创建一个静态文本框
        wx.StaticText(parent=panel, label=u"输入一个整数:", pos=(10,20))
        #创建一个文本框输入框
        self.posCtrl = wx.TextCtrl(parent=panel, pos=(140,20))
         #创建第二个静态文本框
        wx.StaticText(parent=panel, label=u"累计的结果：", pos=(10,80))
        #创建第二个文本框输入框
        self.posCtrl2 = wx.TextCtrl(parent=panel, pos=(140,80))

        #创建一个按钮用于触发计算
        wx.Button(parent=panel,label=u"计算",pos=(10,180))


     #定义按钮的触发函数
    def sum(self,event):
        n = int(self.posCtrl.GetValue() )
        total =0
        for i in range(n+1):
            total = total+i;
        return total;

if __name__ == "__main__":
    total =0
    for i in range(4):
            total = total+i;

    print(total)

    # #创建app对象
    # app = wx.App()
    # #创建框架类对象
    # frame = myFrame()
    # #框架显示
    # frame.Show(True)
    # #创建事物循环
    # app.MainLoop()

