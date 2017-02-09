#encoding:utf-8

"""
对话框
"""
import wx

class myFrame(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,superior,-1,u"使用对话框",size=(500,450))
        #创建pannel
        panel = wx.Panel(self,-1)
        #创建一个button
        self.btnExit = wx.Button(parent=panel,label=u"退出",pos=(300,300),size=(-1,-1))
        #绑定退出按钮的事件
        self.Bind(wx.EVT_BUTTON,self.OnExit,self.btnExit)

    def OnExit(self,event):
        #创建一个对话框
        """
        __init__(self, Window parent, String message, String caption=MessageBoxCaptionStr,
            long style=wxOK|wxCANCEL|wxCENTRE,
            Point pos=DefaultPosition) -> MessageDialog

        Constructor, use `ShowModal` to display the dialog.
        """
        #caption 就是标题
        dialog = wx.MessageDialog(self,u"确认退出吗？",u"退出选择框",style=wx.OK|wx.CANCEL)  #|wx.ICON_QUESTION  如果添加这个就不会显示icon图标
        #对话框的模态显示
        result = dialog.ShowModal()
        print(result)

        if result == wx.ID_OK:
            print(result)
            dialog.Destroy()
            self.Destroy()

if __name__ == "__main__":
    #创建app
    app = wx.App()
    #创建Frame
    frame = myFrame(None)
    #框架显示
    frame.Show(True)
    #创建事件循环
    app.MainLoop()




