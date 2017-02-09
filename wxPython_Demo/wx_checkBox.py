#encoding:utf-8
"""
多选框
"""
import wx

class myFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, superior,-1,u"多选框",pos=(100,200),size=(400,500),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX))
        #创建一个panel
        panel = wx.Panel(self)
        #创建一个静态文本
        wx.StaticText(panel,-1,u"业余爱好",(110,20),style=wx.ALIGN_RIGHT)

        #创建多选框
        self.check1 = wx.CheckBox(panel,id=-1,label=u"旅游",pos=(120,40),size=wx.DefaultSize,style=0,name="CheckBox1")
        self.check1.SetValue(True)
        self.check2 = wx.CheckBox(panel,id=-1,label=u"跑步",pos=(120,70),size=wx.DefaultSize,style=0,name="CheckBox2")
        self.check2.SetValue(True)
        self.check3 = wx.CheckBox(panel,id=-1,label=u"钓鱼",pos=(120,100),size=wx.DefaultSize,style=0,name="CheckBox3")
        self.check3.SetValue(False)

        self.Bind(wx.EVT_CHECKBOX, self.OnClickCheckBox1,self.check1)

    def OnClickCheckBox1(self,event):
        result = self.check1.GetValue();
        print(u"checkbox1的选中状体：%s" % (result))

        #     #关闭所有窗体
        #     #scd.Close()  使用Close方法窗口虽然关闭了，但是资源仍然占用，所以需要是destroy方法。
        #     scd.Destroy()
        #     self.Destroy()

if __name__ == "__main__":
    #创建app
    app = wx.App()
    #创建Frame
    frame = myFrame(None)
    #显示Frame
    frame.Show(True)
    #建立主循环
    app.MainLoop()