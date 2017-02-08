#encoding:utf-8

"""
静态文本StaticText详解
"""
import wx
class myFrame(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,superior, -1, u"示范静态文本框", size=(950,320))
        #创建panel
        panel = wx.Panel(self, -1)
        #创建静态文本框,使用-1生成动态的id
        wx.StaticText(panel,-1,u"Text1：这个默认效果的静态文本框的例子",(100,10))

        rev = wx.StaticText(panel,-1,u"Text2:反向显示静态文本框",(100,30))
        #设置前背景色
        rev.SetForegroundColour("white")
        # 设置后背景色
        rev.SetBackgroundColour("black")

        center = wx.StaticText(panel, -1, u"Text3:文本居中", (100, 50),(260,-1),style=(wx.ALIGN_CENTER))  #第二“-1”是指包裹父窗口的高度|wx.ALIGN_CENTER
        # 设置前背景色
        center.SetForegroundColour("white")
        # 设置后背景色
        center.SetBackgroundColour("black")

        str = wx.StaticText(panel, -1, u"Text4:改变字体", (100, 80),(260,-1),style=(wx.ALIGN_RIGHT))  #第二“-1”是指包裹父窗口的高度|wx.ALIGN_CENTER
        #字体样式
        font = wx.Font(16,wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        #设置字体及字号
        str.SetFont(font)
        # 设置前背景色
        str.SetForegroundColour("white")
        # 设置后背景色
        str.SetBackgroundColour("black")



if __name__ == "__main__":
    #创建app对象
    app = wx.App()
    #创建框架类对象
    frame = myFrame(None)
    #框架显示
    frame.Show(True)
    #创建事物循环
    app.MainLoop()