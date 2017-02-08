#encoding:utf-8

"""
文本输入框详解
"""
import wx

class myFrame(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self, superior , -1, u"文本输入框",pos=(10,10),size=(400, 500))
        #wx.Frame.__init__(self,superior, -1, u"示范静态文本框", size=(950,320))

        #创建一个pannel
        panel = wx.Panel(self, -1);

        #创建文本
        basicStaticLable = wx.StaticText(parent=panel,label=u"Basic Control：" )
        #创建文本输入框
        basicText = wx.TextCtrl(parent=panel,value=u"Python程序设计" ,size=(172,-1))
        #默认选中
        basicText.SetInsertionPoint(0)

        #创建文本
        pwdLabel = wx.StaticText(parent=panel,label="Password: " )
        #创建文本输入框，并指定风格为密码
        pwdText = wx.TextCtrl(parent=panel, value="password",size=(172,-1), style=wx.TE_PASSWORD)

        #FlexGridSizer的layout布局来统一管理其中的控件布局
        #hgap: 子控件之间的水平间隔
        #vgap:子空间之间的垂直间隔
        sizer = wx.FlexGridSizer(rows=2, cols=2, hgap =10, vgap=18)
        #将控件加入到这个layout中
        sizer.AddMany([basicStaticLable,basicText,pwdLabel,pwdText])
        #配置的这个panel隶属于哪个布局
        panel.SetSizer(sizer)

if __name__ == "__main__":
    #创建app对象
    app = wx.App()
    #创建框架类对象
    frame = myFrame(None)
    #框架显示
    frame.Show(True)
    #创建事物循环
    app.MainLoop()
