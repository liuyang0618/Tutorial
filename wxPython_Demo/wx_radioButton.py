#encoding:utf-8
"""
单选按钮
"""
import wx

class myFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, superior,-1,u"单选按钮",pos=(100,200),size=(400,400),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX))
        #创建一个panel
        panel = wx.Panel(self)

        #创建2个window作为2组radioButton组的容器
        window1 = wx.SashWindow(panel,-1,(20,20),(110,120))
        window2 = wx.SashWindow(panel,-1,(155,20),(110,120))

        #创建一个静态文本
        #wx.StaticText(panel,-1,u"业余爱好",(110,20),style=wx.ALIGN_RIGHT)

        #创建单选框
        #radioBox = wx.RadioBox()
        """
        __init__(self, Window parent, int id=-1, String label=EmptyString,
            Point pos=DefaultPosition, Size size=DefaultSize,
            long style=0, Validator validator=DefaultValidator,
            String name=RadioButtonNameStr) -> RadioButton
        """
        #添加单选按钮到对应的window中 ， 注意坐标都是相对于父窗口
        self.radio11 = wx.RadioButton(window1, id=-1,label="radio1",pos=(10,10),size=wx.DefaultSize,style=0,validator=wx.DefaultValidator,name="radio11")
        self.radio11.SetValue(True)
        self.radio12 = wx.RadioButton(window1, id=-1,label=u"跑步",pos=(10,30),size=wx.DefaultSize,style=0,name="radio12")
        self.radio13 = wx.RadioButton(window1, id=-1,label=u"钓鱼",pos=(10,50),size=wx.DefaultSize,style=0,name="radio13")

        self.radio21 = wx.RadioButton(window2,id=-1,label=u"旅游",pos=(10,10),size=wx.DefaultSize,style=0,name="radio21")
        self.radio21.SetValue(True)
        self.radio22 = wx.RadioButton(window2,id=-1,label=u"跑步",pos=(10,30),size=wx.DefaultSize,style=0,name="radio22")
        self.radio23 = wx.RadioButton(window2,id=-1,label=u"钓鱼",pos=(10,50),size=wx.DefaultSize,style=0,name="radio23")


        self.Bind(wx.EVT_RADIOBUTTON, self.OnClickRadioBox1,self.radio11)

    def OnClickRadioBox1(self,event):
        result = self.radio11.GetValue();
        print(u"RadioBox1的选中状体：%s" % (result))

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